import os
import re
import requests
import feedparser
from datetime import datetime

# =========================
# 配置区
# =========================
README_FILE = "README.md"
RESOURCES_FILE = "agent_resources.md"
CHANGELOG_FILE = "CHANGELOG.md"

# GitHub 搜索关键词（可扩展）
SEARCH_QUERIES = [
    "AI Agent framework",
    "multi-agent system",
    "autonomous agent",
    "LLM orchestration",
]

# RSS 源（可以按需扩展）
RSS_FEEDS = [
    "https://www.reddit.com/r/LocalLLaMA/.rss",
    "https://news.ycombinator.com/rss",
    "https://huggingface.co/blog/feed.xml",
]

# 标签映射，用于分类
TAG_MAPPING = {
    "framework": ["framework", "sdk", "library"],
    "memory": ["memory", "vector", "retrieval"],
    "orchestration": ["orchestration", "workflow", "multi-agent"],
    "plugins": ["plugin", "tools", "integration"],
    "runtime": ["runtime", "execution", "engine"],
    "rss": ["rss", "blog", "news", "release"],  # 新增 RSS 分类
}

# GitHub API
GITHUB_API = "https://api.github.com/search/repositories"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")  # 需要 GitHub Token


# =========================
# 工具函数
# =========================
def github_search(query, per_page=10):
    """调用 GitHub API 搜索项目"""
    headers = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    params = {"q": query, "sort": "stars", "order": "desc", "per_page": per_page}
    resp = requests.get(GITHUB_API, headers=headers, params=params)

    if resp.status_code != 200:
        print(f"GitHub API 调用失败: {resp.status_code}, {resp.text}")
        return []

    return resp.json().get("items", [])


def parse_rss_feed(url, limit=5):
    """解析 RSS 源，返回最新的若干条"""
    try:
        feed = feedparser.parse(url)
    except Exception as e:
        print(f"RSS 解析失败 {url}: {e}")
        return []

    items = []
    for entry in feed.entries[:limit]:
        items.append(
            {
                "name": entry.get("title", "Untitled"),
                "html_url": entry.get("link", ""),
                "description": entry.get("summary", "")[:200],
                "stargazers_count": 0,  # RSS 没有 stars 字段
                "source": "rss",
            }
        )
    return items


def classify_repo(repo):
    """根据关键词分类"""
    name = repo["name"].lower()
    desc = (repo["description"] or "").lower()
    tags = []
    for tag, keywords in TAG_MAPPING.items():
        if any(k in name or k in desc for k in keywords):
            tags.append(tag)
    if not tags:
        tags.append("misc")
    return tags


def load_static_links(filename=README_FILE):
    """读取 README 静态区的所有链接，避免重复"""
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # 找到自动更新区
    dynamic_section_pattern = re.compile(
        r"<!-- AGENT-INFRA-START -->(.*?)<!-- AGENT-INFRA-END -->",
        re.DOTALL,
    )
    dynamic_section = dynamic_section_pattern.findall(content)
    if dynamic_section:
        dynamic_content = dynamic_section[0]
    else:
        dynamic_content = ""

    # 静态区 = 全部内容 - 动态区
    static_content = content.replace(dynamic_content, "")

    # 提取所有 markdown 链接 (https://xxx)
    urls = set(re.findall(r"\(https?://[^\)]+?\)", static_content))
    return urls


def generate_markdown(resources_by_tag):
    """生成资源列表 Markdown"""
    md = []
    for tag, repos in resources_by_tag.items():
        if not repos:
            continue
        md.append(f"### {tag.capitalize()}\n")
        for r in repos:
            stars = f" ⭐{r['stargazers_count']}" if r["stargazers_count"] else ""
            md.append(f"- [{r['name']}]({r['html_url']}){stars}\n  - {r['description'] or 'No description'}\n")
        md.append("\n")
    return "".join(md)


def update_readme(resources_markdown):
    """更新 README.md 自动更新区"""
    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(
        r"(<!-- AGENT-INFRA-START -->)(.*?)(<!-- AGENT-INFRA-END -->)",
        f"\\1\n{resources_markdown}\n\\3",
        content,
        flags=re.DOTALL,
    )

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)


def update_changelog(new_items):
    """更新 CHANGELOG.md"""
    date_str = datetime.utcnow().strftime("%Y-%m-%d")
    lines = [f"## {date_str}\n"]
    for r in new_items:
        stars = f" ⭐{r['stargazers_count']}" if r["stargazers_count"] else ""
        lines.append(f"- Added [{r['name']}]({r['html_url']}){stars}")
    lines.append("\n")

    if os.path.exists(CHANGELOG_FILE):
        with open(CHANGELOG_FILE, "r", encoding="utf-8") as f:
            old = f.read()
    else:
        old = ""

    with open(CHANGELOG_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n" + old)


# =========================
# 主逻辑
# =========================
def main():
    all_repos = []

    # GitHub 搜索
    for q in SEARCH_QUERIES:
        repos = github_search(q)
        for r in repos:
            r["source"] = "github"
        all_repos.extend(repos)

    # RSS 订阅
    for url in RSS_FEEDS:
        items = parse_rss_feed(url)
        all_repos.extend(items)

    print(f"共获取 {len(all_repos)} 个项目（未去重）")

    # 去重
    seen_urls = set()
    unique_items = []
    for r in all_repos:
        if r["html_url"] not in seen_urls:
            unique_items.append(r)
            seen_urls.add(r["html_url"])

    print(f"去重后剩余 {len(unique_items)} 个项目")

    # 静态去重：过滤掉 README.md 静态区已有的链接
    static_links = load_static_links()
    filtered_items = [r for r in unique_items if f"({r['html_url']})" not in static_links]

    print(f"过滤静态区后剩余 {len(filtered_items)} 个项目")

    # 分类
    resources_by_tag = {k: [] for k in TAG_MAPPING.keys()}
    resources_by_tag["misc"] = []
    for r in filtered_items:
        tags = classify_repo(r)
        for t in tags:
            resources_by_tag[t].append(r)

    # 生成 Markdown
    resources_md = generate_markdown(resources_by_tag)

    # 更新 README
    update_readme(resources_md)

    # 更新 agent_resources.md（全量，不去重）
    full_resources_by_tag = {k: [] for k in TAG_MAPPING.keys()}
    full_resources_by_tag["misc"] = []
    for r in unique_items:
        tags = classify_repo(r)
        for t in tags:
            full_resources_by_tag[t].append(r)
    full_md = generate_markdown(full_resources_by_tag)
    with open(RESOURCES_FILE, "w", encoding="utf-8") as f:
        f.write("# Agent Infra Resources\n\n" + full_md)

    # 更新 CHANGELOG
    update_changelog(filtered_items)


if __name__ == "__main__":
    main()

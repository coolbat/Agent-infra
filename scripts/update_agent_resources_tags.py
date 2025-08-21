import requests, os, feedparser
from jinja2 import Template
from datetime import datetime

# ---------- 配置 ----------
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
MAX_RESULTS = 30
README_FILE = "README.md"
MD_FILE = "agent_resources.md"
CHANGELOG_FILE = "CHANGELOG.md"

HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

# GitHub 搜索关键字
SEARCH_QUERIES = {
    "Runtime": "AI Agent runtime in:description",
    "Memory": "AI Agent memory database in:description",
    "Orchestration": "AI Agent orchestration workflow in:description",
    "Tools": "AI Agent plugin tools in:description",
    "Security": "AI Agent security in:description",
    "Observability": "AI Agent observability monitoring in:description"
}

# 多标签映射，可以自定义扩展
TAG_MAPPING = {
    "Runtime": ["Runtime"],
    "Memory": ["Memory"],
    "Orchestration": ["Orchestration"],
    "Tools": ["Plugin", "Tools"],
    "Security": ["Security"],
    "Observability": ["Observability", "Monitoring"]
}

# RSS 订阅示例
RSS_FEEDS = [
    "https://www.agentblog.com/rss"  # 替换为真实 RSS
]

# ---------- GitHub 搜索 ----------
def search_github(query):
    url = f"https://api.github.com/search/repositories?q={query}&per_page={MAX_RESULTS}"
    resp = requests.get(url, headers=HEADERS)
    items = []
    for i in resp.json().get("items", []):
        if i["stargazers_count"] < 5:
            continue
        items.append({
            "name": i["name"],
            "url": i["html_url"],
            "description": i["description"] or "",
            "tags": [],
            "category": "",
            "stars": i["stargazers_count"],
            "last_updated": i["updated_at"]
        })
    return items

def fetch_all_github_resources():
    all_resources, seen_urls = [], set()
    for category, query in SEARCH_QUERIES.items():
        results = search_github(query)
        for r in results:
            if r["url"] in seen_urls:
                continue
            r["category"] = category
            r["tags"] = TAG_MAPPING.get(category, [])
            seen_urls.add(r["url"])
            all_resources.append(r)
    return all_resources

# ---------- RSS 资源 ----------
def fetch_rss_resources():
    rss_resources = []
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            rss_resources.append({
                "name": entry.title,
                "url": entry.link,
                "description": getattr(entry, "summary", ""),
                "category": "Blog/News",
                "tags": ["Blog", "News"],
                "stars": None,
                "last_updated": getattr(entry, "published", "")
            })
    return rss_resources

# ---------- Markdown 生成 ----------
def generate_markdown(resources, filename):
    template_str = """
{% set tag_groups = {} %}
{% for r in resources %}
    {% for tag in r.tags %}
        {% if tag not in tag_groups %}{% set _ = tag_groups.update({tag: []}) %}{% endif %}
        {% set _ = tag_groups[tag].append(r) %}
    {% endfor %}
{% endfor %}

{% for tag, items in tag_groups.items() %}
### {{ tag }}

{% for r in items|sort(attribute='stars', reverse=True) %}
- [{{ r.name }}]({{ r.url }}) – {{ r.description }}
{% endfor %}

{% endfor %}
"""
    template = Template(template_str)
    md_content = template.render(resources=resources)
    with open(filename, "w", encoding="utf-8") as f: f.write(md_content)
    return md_content

# ---------- README 更新 ----------
def update_readme(md_content, filename=README_FILE):
    start_marker = "<!-- AGENT-INFRA-START -->"
    end_marker = "<!-- AGENT-INFRA-END -->"
    with open(filename, "r", encoding="utf-8") as f: content = f.read()
    before, after = content.split(start_marker)[0], content.split(end_marker)[1]
    new_content = before + start_marker + "\n" + md_content + "\n" + end_marker + after
    with open(filename, "w", encoding="utf-8") as f: f.write(new_content)

# ---------- CHANGELOG ----------
def update_changelog(resources, filename=CHANGELOG_FILE):
    date_str = datetime.utcnow().strftime("%Y-%m-%d")
    new_entries = "\n".join([f"- [{r['name']}]({r['url']}) – {r['description']}" for r in resources])
    entry = f"## {date_str}\n\n{new_entries}\n\n"
    content = ""
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f: content = f.read()
    with open(filename, "w", encoding="utf-8") as f: f.write(entry + content)

# ---------- 主程序 ----------
if __name__ == "__main__":
    print("🔍 Fetching GitHub resources...")
    github_resources = fetch_all_github_resources()
    print(f"⚡ Fetched {len(github_resources)} GitHub items")

    print("🔍 Fetching RSS resources...")
    rss_resources = fetch_rss_resources()
    print(f"⚡ Fetched {len(rss_resources)} RSS items")

    all_resources = github_resources + rss_resources

    print("📝 Generating Markdown...")
    md_content = generate_markdown(all_resources, MD_FILE)

    print("📄 Updating README...")
    update_readme(md_content)

    print("📜 Updating CHANGELOG...")
    update_changelog(all_resources)

    print(f"✅ Done! Updated {MD_FILE}, README.md, and CHANGELOG.md")

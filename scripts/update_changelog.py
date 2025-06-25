# scripts/update_changelog.py
import feedparser
import html
import os
import pathlib
import datetime
import re

# Full version tag, e.g., 5.1.1-1 → extract just 5.1.1
docker_tag = os.environ["VERSION"]
version = docker_tag.split("-")[0]

# Parse Atom feed
feed = feedparser.parse("https://www.qbittorrent.org/news_feed.atom")

# Find matching release entry by version in title
entry = next((e for e in feed.entries if f"v{version}" in e.title), None)

if entry:
    raw_html = entry.get("content", [{}])[0].get("value", "")
    changelog = html.unescape(raw_html)
else:
    changelog = f"No changelog found for version {version}"

# Compose markdown header
header = f"## v{docker_tag} – {datetime.date.today()}\n\n{changelog}\n\n"

# Prepend to CHANGELOG.md (if not already there)
path = pathlib.Path("./qbittorrent_nox/CHANGELOG.md")
if path.exists():
    content = path.read_text(encoding="utf-8")
    if not re.search(rf"^##\s+v{re.escape(docker_tag)}\b", content, re.M):
        path.write_text(header + content, encoding="utf-8")
else:
    path.write_text("# qBittorrent-Nox Add-on Changelog\n\n" + header, encoding="utf-8")

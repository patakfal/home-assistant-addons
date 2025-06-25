# scripts/update_changelog.py
import feedparser, html, os, pathlib, datetime, re

ver = os.environ["VERSION"]
feed = feedparser.parse("https://www.qbittorrent.org/news_feed.atom")

summary = next((html.unescape(e.summary) for e in feed.entries if ver in e.title), "")
if not summary:
    summary = f"No changelog found for v{ver}"

path = pathlib.Path("./qbittorrent_nox/CHANGELOG.md")
header = f"## v{ver} – {datetime.date.today()}\n\n{summary}\n\n"

if path.exists():
    content = path.read_text(encoding="utf-8")
    if not re.search(rf"^##\s+v{re.escape(ver)}\b", content, re.M):
        path.write_text(header + content, encoding="utf-8")
else:
    path.write_text("# qBittorrent-Nox Add-on Changelog\n\n" + header, encoding="utf-8")
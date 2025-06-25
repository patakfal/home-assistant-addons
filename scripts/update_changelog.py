# scripts/update_changelog.py
import feedparser, html, os, pathlib, datetime, re

# Full Docker tag, e.g. "5.1.1-1"
full_version = os.environ["VERSION"]

# Extract "5.1.1" (ignore "-1" or any suffix)
semver = full_version.split("-")[0]

# Load Atom feed
feed = feedparser.parse("https://www.qbittorrent.org/news_feed.atom")

# Try to match "qBittorrent v5.1.1 release"
summary = next(
    (html.unescape(e.summary) for e in feed.entries if semver in e.title),
    f"No changelog found for v{semver}"
)

# Target file
path = pathlib.Path("./qbittorrent_nox/CHANGELOG.md")
header = f"## v{full_version} – {datetime.date.today()}\n\n{summary}\n\n"

# Write/prepend
if path.exists():
    content = path.read_text(encoding="utf-8")
    if not re.search(rf"^##\s+v{re.escape(full_version)}\b", content, re.M):
        path.write_text(header + content, encoding="utf-8")
else:
    path.write_text("# qBittorrent-Nox Add-on Changelog\n\n" + header, encoding="utf-8")

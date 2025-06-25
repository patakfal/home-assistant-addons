#!/usr/bin/env python3
"""
Write the qBittorrent release notes for the Docker tag in $VERSION
into ./CHANGELOG.md, placing the newest entry directly after the main
file heading so it always appears first.
"""
import feedparser
import html
import os
import pathlib
import datetime as dt
import re
import sys

# ----------------------------------------------------------------------
# 1 Figure out the versions we care about
# ----------------------------------------------------------------------
docker_tag = os.environ.get("VERSION")
semver = docker_tag.split("-")[0]                    # "5.1.1"

# ----------------------------------------------------------------------
# 2 Pull Atom feed and find the matching entry
# ----------------------------------------------------------------------
feed = feedparser.parse("https://www.qbittorrent.org/news_feed.atom")
entry = next((e for e in feed.entries if f"v{semver}" in e.title), None)

if entry:
    raw_html  = entry.get("content", [{}])[0].get("value", "")
    changelog_body = html.unescape(raw_html)
else:
    changelog_body = f"No changelog found for version {semver}"

# ----------------------------------------------------------------------
# 3 Prepare the markdown block we’ll insert
# ----------------------------------------------------------------------
header_block = (
    f"## v{docker_tag} – {dt.date.today()}\n\n"
    f"{changelog_body}\n\n"
)

# ----------------------------------------------------------------------
# 4 Write (or prepend) to CHANGELOG.md
# ----------------------------------------------------------------------
path = pathlib.Path("./qbittorrent_nox/CHANGELOG.md")
main_heading = "# qBittorrent-Nox Add-on Changelog"

if not path.exists():
    # First run: create file with heading and first entry
    path.write_text(f"{main_heading}\n\n{header_block}", encoding="utf-8")
    sys.exit(0)

content = path.read_text(encoding="utf-8")

# If this exact docker_tag is already present, do nothing
if re.search(rf"^##\s+v{re.escape(docker_tag)}\b", content, re.M):
    sys.exit(0)

# Split off (or create) the main heading
if content.startswith(main_heading):
    heading_line, remainder = content.split("\n", 1)
    new_content = f"{heading_line}\n\n{header_block}{remainder.lstrip()}"
else:
    # File exists but has no main heading for some reason – just prepend
    new_content = f"{main_heading}\n\n{header_block}{content}"

path.write_text(new_content, encoding="utf-8")

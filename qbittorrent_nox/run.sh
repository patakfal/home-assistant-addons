#!/bin/sh
set -e

# Ensure required directories exist
mkdir -p /config /downloads

# Start qBittorrent-Nox
exec qbittorrent-nox --webui-port=$QBT_WEBUI_PORT

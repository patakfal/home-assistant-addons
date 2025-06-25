#!/bin/sh
set -e

# Ensure required directories exist
mkdir -p /config/qBittorrent

# Start qBittorrent-Nox
exec qbittorrent-nox --webui-port=$QBT_WEBUI_PORT --profile=/config

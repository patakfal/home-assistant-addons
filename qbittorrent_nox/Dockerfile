# Use the official qbittorrent-nox image as base
FROM qbittorrentofficial/qbittorrent-nox:5.1.0

# Set environment variables
ENV QBT_EULA=ACCEPTEULA \
    QBT_VERSION=latest \
    QBT_WEBUI_PORT=8080 \
    TZ=UTC \
    HOME=/data

# Set working directory
WORKDIR /config

# Expose necessary ports
EXPOSE 6881/tcp 6881/udp 8080/tcp

# Make /tmp a tmpfs mount point
VOLUME /tmp

# Create necessary directories
RUN mkdir -p /config /downloads

# Copy start script
COPY run.sh /run.sh
RUN chmod +x /run.sh

# Set entrypoint
ENTRYPOINT ["/run.sh"]


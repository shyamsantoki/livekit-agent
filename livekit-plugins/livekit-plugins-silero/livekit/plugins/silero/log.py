import logging

logger = logging.getLogger("livekit.plugins.silero")

# Suppress DEBUG logs from the 'websockets' package
logging.getLogger("websockets").setLevel(logging.INFO)

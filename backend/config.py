# backend/config.py

import os

# WebSocket server configuration
WS_HOST = os.getenv('WS_HOST', '0.0.0.0')
WS_PORT = int(os.getenv('WS_PORT', 8765))

# HTTP server configuration
HTTP_HOST = os.getenv('HTTP_HOST', 'localhost')
HTTP_PORT = int(os.getenv('HTTP_PORT', 8000))

# Transcription service configuration
TRANSCRIPTION_HOST = os.getenv('TRANSCRIPTION_HOST', '192.168.86.55')
TRANSCRIPTION_PORT = int(os.getenv('TRANSCRIPTION_PORT', 9090))
TRANSCRIPTION_MODEL = os.getenv('TRANSCRIPTION_MODEL', 'small')
USE_VAD = os.getenv('USE_VAD', 'True').lower() == 'true'

# Audio configuration
CHUNK = 1024
FORMAT = 'int16'
CHANNELS = 1
RATE = 16000
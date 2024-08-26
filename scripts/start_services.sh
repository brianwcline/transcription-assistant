#!/bin/bash

# Start the backend server
cd /path/to/transcription-assistant/backend
source venv/bin/activate
python audio_server.py &

# Start the frontend
cd /path/to/transcription-assistant/frontend
npm run start &

echo "Services started!"
#!/bin/bash

# Update and upgrade the system
sudo apt update && sudo apt upgrade -y

# Install required system packages
sudo apt install -y python3-venv nodejs npm nginx

# Set up the backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate

# Set up the frontend
cd ../frontend
npm install

# Build the frontend
npm run build

# Set up nginx
sudo cp /path/to/your/nginx/config /etc/nginx/sites-available/transcription-assistant
sudo ln -s /etc/nginx/sites-available/transcription-assistant /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx

echo "Installation complete!"
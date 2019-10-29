SERVICE_NAME=growbothub-daq.service
SERVICE_PATH=/etc/systemd/system/${SERVICE_NAME}

# Populate service file
sudo bash -c "cat > ${SERVICE_PATH}" << EOF
[Unit]
Description=GrowbotHub DAQ

[Service]
User=pi
ExecStart=/usr/bin/python3 $(pwd)/daq.py

[Install]
WantedBy=multi-user.target
EOF

sudo chmod 664 ${SERVICE_PATH}
sudo systemctl daemon-reload
sudo systemctl enable ${SERVICE_NAME}
sudo systemctl start ${SERVICE_NAME}

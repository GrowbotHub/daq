# Scripts for Dataset Acquisition

## Verify if camera works
```
raspistill -o image.jpg
```

## Dependencies
```
apt install python3-gpiozero python3-smbus python3-picamera
```

## Quick start
Create systemd configuration file and enable the service:
```
./configure.sh
```
verify if everything is running properly:
```
systemctl status growbothub-daq.service
```
and if you want to stop:
```
systemctl stop growbothub-daq.service
```

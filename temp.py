# Reference: https://github.com/ControlEverythingCommunity/TH02

import smbus
import time

bus = smbus.SMBus(1)

# Read temperature
bus.write_byte_data(0x40, 0x03, 0x11)
time.sleep(0.5)
data = bus.read_i2c_block_data(0x40, 0x00, 3)
temp = ((data[1] * 256 + (data[2] & 0xFC))/ 4.0) / 32.0 - 50.0

# Read humidty
bus.write_byte_data(0x40, 0x03, 0x01)
time.sleep(0.5)
data = bus.read_i2c_block_data(0x40, 0x00, 3)
humidity = ((data[1] * 256 + (data[2] & 0xF0)) / 16.0) / 16.0 - 24.0
humidity = humidity - (((humidity * humidity) * (-0.00393)) + (humidity * 0.4008) - 4.7844)
humidity = humidity + (temp - 30) * (humidity * 0.00237 + 0.1973)

# Output data to screen
print("Relative Humidity : %.2f %%" % humidity)
print("Temperature in Celsius : %.2f C" % temp)

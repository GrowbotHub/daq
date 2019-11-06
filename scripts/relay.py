from gpiozero.pins.native import NativeFactory
from gpiozero import Device, DigitalOutputDevice
from time import sleep

Device.pin_factory = NativeFactory()

relay = DigitalOutputDevice(5)

while True:
  relay.toggle()
  sleep(1)


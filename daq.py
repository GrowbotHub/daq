from picamera import PiCamera
from time import sleep
from datetime import datetime
import os

DIST = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')
PERIOD_HOURS = 1


def get_filepath():
	now = datetime.now()
	timestamp = now.strftime('%y-%m-%d_%H-%M-%S')
	img_name = 'image_{}.jpg'.format(timestamp)
	return os.path.join(DIST, img_name)
	

def take_picture(camera):
	filepath = get_filepath()
	camera.capture(filepath)
	print('New image saved to `{}`'.format(filepath))


def main():
	if not os.path.exists(DIST):
		os.makedirs(DIST)

	print('Initializing camera...')
	camera = PiCamera()
	print('Camera initialized')
	while True:
		take_picture(camera)
		sleep(60 * 60 * PERIOD_HOURS)


if __name__ == '__main__':
	main()


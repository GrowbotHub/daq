from PIL import Image
import glob, os
import tensorflow as tf
import numpy as np
from time import time


TEST_DIR = 'dataset-growth-stage-radish/dataset/test'


# Load model
interpreter = tf.lite.Interpreter(model_path="radishes.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Prepare image
infile = glob.glob(os.path.join(TEST_DIR, 'small/*.jpg'))[10]
f, ext = os.path.splitext(infile)
im = Image.open(infile)
im = im.resize(input_details[0]['shape'][1:3])
im = np.array(im).reshape(input_details[0]['shape'])

# Classify
tic = time()
interpreter.set_tensor(input_details[0]['index'], im.astype(np.float32))
interpreter.invoke()
toc = time()
required_time = round(toc - tic, 3) * 1000

# Print the result
output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data, required_time, 'ms')

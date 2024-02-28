from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from io import BytesIO
import requests

class NSFWDetector:
	"""
	A class for predicting whether an image contains NSFW content using a pre-trained model.

	"""

	def __init__(self, model_path):
		self.model_path = model_path
		self.model = load_model(model_path)
		self.img_size = (299, 299)

	def predict_from_image(self, image_data):
		try:
			img = image_data.resize(self.img_size)
			img_array = image.img_to_array(img)
			img_array = np.expand_dims(img_array, axis=0)
			img_array /= 255.0 

			predictions = self.model.predict(img_array)

			binary_prediction = int(np.round(predictions[0]))

			return not binary_prediction

		except Exception as e:
			return 'error' + str(e)

	def predict(self, path):
		try:
			if path.startswith('http'):
				response = requests.get(path)
				img = Image.open(BytesIO(response.content))
			else:
				img = Image.open(path)

			return self.predict_from_image(img)
		except Exception as e:
			return str(e)

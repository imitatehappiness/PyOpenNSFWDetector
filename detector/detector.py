from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from io import BytesIO
import requests

class ImagePredictor:
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

	def predict_from_url(self, url):
		try:
			response = requests.get(url)
			img = Image.open(BytesIO(response.content))
			return self.predict_from_image(img)
		except Exception as e:
			return str(e)

	def predict_from_file(self, file_path):
		try:
			img = Image.open(file_path)
			return self.predict_from_image(img)
		except Exception as e:
			return str(e)
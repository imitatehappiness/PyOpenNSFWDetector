from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from io import BytesIO
import requests

class ImagePredictor:
	"""
	A class for predicting whether an image contains NSFW content using a pre-trained model.

	Attributes
	----------
	model_path : str
		The path to the pre-trained model.
	model : tensorflow.keras.models.Model
		The loaded pre-trained model.
	img_size : tuple
		The size to which images are resized before prediction.
	"""

	def __init__(self, model_path):
		"""
		Initialize the ImagePredictor class with the path to the model.

		Parameters
		----------
		model_path : str
			The path to the pre-trained model.
		"""
		self.model_path = model_path
		self.model = load_model(model_path)
		self.img_size = (299, 299)

	def predict_from_image(self, image_data):
		"""
		Predict whether an image contains NSFW content.

		Parameters
		----------
		image_data : PIL.Image.Image
			The image data as a PIL Image object.

		Returns
		-------
		bool
			True if the image contains NSFW content, False otherwise.
		"""
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
		"""
		Predict whether an image from a URL contains NSFW content.

		Parameters
		----------
		url : str
			The URL of the image.

		Returns
		-------
		bool
			True if the image contains NSFW content, False otherwise.
		"""
		try:
			response = requests.get(url)
			img = Image.open(BytesIO(response.content))
			return self.predict_from_image(img)
		except Exception as e:
			return str(e)

	def predict_from_file(self, file_path):
		"""
		Predict whether an image from a file contains NSFW content.

		Parameters
		----------
		file_path : str
			The path to the image file.

		Returns
		-------
		bool
			True if the image contains NSFW content, False otherwise.
		"""
		try:
			img = Image.open(file_path)
			return self.predict_from_image(img)
		except Exception as e:
			return str(e)

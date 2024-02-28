import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'detector')))
from detector import NSFWPredictor

class TestImagePredictor(unittest.TestCase):
	def setUp(self):
		self.model_path = 'model/nude_detector_model.h5'
		self.predictor = NSFWPredictor(self.model_path)

	def test_predict_from_url(self):
		print("\n[TEST] predict_from_url")

		# Test with adult content
		path = 'https://s.pfst.net/2024.02/8081984667080bec99cc7d12e65a5c11aa8a70ef9cefc_b.jpg'
		self.assertEqual(self.predictor.predict_from_url(path), 1)

		path = 'https://s.pfst.net/2024.02/808198266708058ac317a4b25227bbb7a3be9d969b0bf_b.jpg'
		self.assertEqual(self.predictor.predict_from_url(path), 1)

		path = 'https://s.pfst.net/2024.02/8082043667080f8694f2843edb8fe2bb858aa21bd8cab_b.jpg'
		self.assertEqual(self.predictor.predict_from_url(path), 1)

		# Test with regular content
		path = 'https://s.pfst.net/2022.08/6971621667080909e89391f886395410b385c888ab881_b.jpg'
		self.assertEqual(self.predictor.predict_from_url(path), 0)

		path = 'https://s.pfst.net/2022.08/6971622667080f69396f3d8a776df8f8730a53517e6ae_b.jpg'
		self.assertEqual(self.predictor.predict_from_url(path), 0)

		path = 'https://s.pfst.net/2022.08/6971623667080efa9d3d417abbdba08ad09cade77961b_b.jpg'
		self.assertEqual(self.predictor.predict_from_url(path), 0)

	def test_predict_from_file(self):
		print("\n[TEST] predict_from_file")
		
		# Test with adult content
		path = 'resources\\local_image_adult.jpg'
		self.assertEqual(self.predictor.predict_from_file(path), 1)

		# Test with regular content
		path = 'resources\\local_image_regular.jpg'
		self.assertEqual(self.predictor.predict_from_file(path), 0)

if __name__ == '__main__':
	unittest.main()

from detector.detector import ImagePredictor

model_path = 'model/nude_detector_model.h5'
predictor = ImagePredictor(model_path)

path = 'https://s.pfst.net/2024.02/8081984667080bec99cc7d12e65a5c11aa8a70ef9cefc_b.jpg'
print("predict:", predictor.predict_from_url(path))

path = 'https://s.pfst.net/2022.08/6971621667080909e89391f886395410b385c888ab881_b.jpg'
print("predict:", predictor.predict_from_url(path))

path = "resources\\local_image_adult.jpg"
print("predict:", predictor.predict_from_file(path))

path = "resources\\local_image_regular.jpg"
print("predict:", predictor.predict_from_file(path))
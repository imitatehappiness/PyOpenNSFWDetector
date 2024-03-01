from detector.detector import NSFWDetector
import time
from datetime import datetime
import logging

logging.basicConfig(filename='nsfw_detector.log', level=logging.INFO, format='%(asctime)s - %(message)s')

start_time = time.time()
logging.info(f"START")

model_path = 'model/nude_detector_model.h5'
NSFW_detector = NSFWDetector(model_path)

paths_regular = [
    'https://s.pfst.net/2022.08/70055736670802f84a85b2eb23a7c5db81414ac2efd9e_b.jpg',
    'https://s.pfst.net/2022.08/7004626667080564f4b05c15e62c5d8f8f01c1122d103_b.jpg',
    'https://s.pfst.net/2022.08/6973122667080627f2a9415750890c6be332ec44bdf64_b.jpg',
    'https://s.pfst.net/2022.08/6973126667080c09fd773f8b050780cd7e22231ab10f5_b.jpg',
    'https://s.pfst.net/2022.08/6972629667080c7a152f747f2615a44ff1512d2a207b5_b.jpg',
    'https://s.pfst.net/2022.08/99926566708064b01cfbe1c35b881da4e11edb145c9a_b.jpg',
    'https://s.pfst.net/2022.08/6973120667080fae6f750d00f01eb27bbd451c15982b1_b.jpg',
    'https://s.pfst.net/2022.08/69736376670805dc122e54a55a02ac2fbff71e70a356e_b.jpg',
    'https://s.pfst.net/2022.08/69736296670807ed6ba90e3e9a15df9b26dee66f0d6ab_b.jpg',
    'https://s.pfst.net/2022.08/69736446670806a6907debdf205521352f5301cffe667_b.jpg'
]

paths_adult = [
    'https://s.pfst.net/2022.08/7017988667080508b204c30f3840629f220dd8ee3231d_b.jpg',
    'https://s.pfst.net/2022.08/70179896670807987f5ec88a0e56894a2eaad54d4702e_b.jpg',
    'https://s.pfst.net/2022.08/7023797667080130bd9e5f66784c24eb328cf0c6de215_b.jpg',
    'https://s.pfst.net/2022.08/702379666708026d401fa1b4d39e6615962b55a835012_b.jpg',
    'https://s.pfst.net/2022.08/710119266708005bf92bb55123abd500c11f2f4468988_b.jpg',
    'https://s.pfst.net/2022.08/6977032667080f06b69fab7e4e318884fa8b0c1719e4c_b.jpg',
    'https://s.pfst.net/2022.08/7211902667080c3a2776108e1d906d5b5ecdb24748791_b.jpg',
    'https://s.pfst.net/2022.08/7213909667080b84431cf352e6166ee6ff237b2d65806_b.jpg'
]

# Предсказание для одного изображения
start_time = time.time()
path = 'https://s.pfst.net/2022.08/6971621667080909e89391f886395410b385c888ab881_b.jpg'
NSFW_detector.predict(path)
end_time = time.time()
logging.info(f"Execution time for 1 image: {end_time - start_time} seconds")

# Предсказание для 10 изображений
start_time = time.time()
for _ in range(10):
	NSFW_detector.predict(path)
end_time = time.time()
logging.info(f"Execution time for 10 images: {end_time - start_time} seconds")

# Предсказание для 100 изображений
start_time = time.time()
for _ in range(100):
	NSFW_detector.predict('https://s.pfst.net/2022.08/6971621667080909e89391f886395410b385c888ab881_b.jpg')
end_time = time.time()
logging.info(f"Execution time for 100 images: {end_time - start_time} seconds")

# Предсказание для 1000 изображений
start_time = time.time()
for _ in range(1000):
	NSFW_detector.predict('https://s.pfst.net/2022.08/6971621667080909e89391f886395410b385c888ab881_b.jpg')
end_time = time.time()
logging.info(f"Execution time for 1000 images: {end_time - start_time} seconds\n")
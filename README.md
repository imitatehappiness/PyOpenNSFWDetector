
![title](https://github.com/imitatehappiness/PyOpenNSFWDetector/assets/79199956/b06bee1b-86e4-42ad-a67a-f245d29110bb)


# PyOpenNSFWDetector

PyOpenNSFWDetector is a project that uses machine learning to detect **NSFW (Not Safe For Work)** content in photos. It can be useful for content filtering on social media, online stores, and other platforms where content control is required.

### The result has binary values: 
* 0 if there is no NSFW content in the photo
* 1 if NSFW content is detected.

## Quick start
```bash
git clone https://github.com/imitatehappiness/PyOpenNSFWDetector.git
cd PyOpenNSFWDetector
pip install -r requirements.txt
python example.py 
```
# Examples
## 1. Example Usage

```python
from detector.detector import NSFWDetector

model_path = 'model/nude_detector_model.h5'
NSFW_detector = NSFWDetector(model_path)

# url path
path = 'https://s.pfst.net/2024.02/8081984667080bec99cc7d12e65a5c11aa8a70ef9cefc_b.jpg'
print("predict:", NSFW_detector.predict(path))

path = 'https://s.pfst.net/2022.08/6971621667080909e89391f886395410b385c888ab881_b.jpg'
print("predict:", NSFW_detector.predict(path))

# local path
path = "resources\\local_image_adult.jpg"
print("predict:", NSFW_detector.predict(path))

path = "resources\\local_image_adult.jpg"
print("predict:", NSFW_detector.predict(path))
```

### Execution time
```
Execution time for 1 image: 1.008302927017212 seconds

Execution time for 10 images: 2.7786076068878174 seconds

Execution time for 100 images: 28.80970525741577 seconds

Execution time for 1000 images: 287.2076916694641 seconds
```

## 2. Example Usage (API)
```python
from detector.detector import NSFWDetector
from flask import Flask, jsonify, request

model_path = 'model/nude_detector_model.h5'
NSFW_detector = NSFWDetector(model_path)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
	url = request.json.get('url')
	prediction = NSFW_detector.predict(url)
	return jsonify({'prediction': prediction})

if __name__ == '__main__':
	app.run(debug=True)
```

# API
### /predict (POST)
```
curl -X POST -H "Content-Type: application/json" -d '{"url": "https://example.com/image.jpg"}' http://127.0.0.1:5000/predict
```

## Model

Model from [NSFWGuard](https://github.com/midhunsankar23/NSFWGuard/tree/main)

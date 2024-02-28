

# PyNudeDetector

PyNudeDetector is a project that uses machine learning to detect nudity in photos. It can be useful for content filtering on social media, online stores, and other platforms where content control is required.

### The result has binary values: 
* 0 if there is no nudity in the photo
* 1 if nudity is detected.

## Quick start
```bash
git clone https://github.com/imitatehappiness/PyNudeDetector.git
cd PyNudeDetector
pip install -r requirements.txt
python example.py 
```
## Example Usage

```python
from detector.detector import ImagePredictor

model_path = 'model/nude_detector_model.h5'
predictor = ImagePredictor(model_path)

path = 'https://s.pfst.net/2024.02/8081984667080bec99cc7d12e65a5c11aa8a70ef9cefc_b.jpg'
print("predict:", predictor.predict_from_url(path))

path = 'https://s.pfst.net/2022.08/6971621667080909e89391f886395410b385c888ab881_b.jpg'
print("predict:", predictor.predict_from_url(path))

path = "resources\\local_image_adult.jpg"
print("predict:", predictor.predict_from_file(path))

path = "resources\\local_image_adult.jpg"
print("predict:", predictor.predict_from_file(path))

```


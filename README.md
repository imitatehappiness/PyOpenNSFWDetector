
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
## Example Usage

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
## Model

Model from [NSFWGuard](https://github.com/midhunsankar23/NSFWGuard/tree/main)

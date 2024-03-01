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

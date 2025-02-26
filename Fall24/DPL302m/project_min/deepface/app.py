from flask import Flask, request, jsonify
from deepface import DeepFace
from flask_cors import CORS
import io
import base64
import numpy as np
from PIL import Image

app = Flask(__name__)
CORS(app)

@app.route('/verify', methods=['POST'])
def verify():
    try:
        # Get data from the request
        data = request.get_json()
        img1_base64 = 'data:image/jpeg;base64,' + data['image1']
        img2_base64 = 'data:image/jpeg;base64,' + data['image2']
        model_name = data['model_name']

        # Decode base64 images to NumPy arrays
        img1_bytes = base64.b64decode(img1_base64.split(',')[1])
        img2_bytes = base64.b64decode(img2_base64.split(',')[1])

        # Convert bytes to RGB images using PIL and then to NumPy arrays
        img1 = np.array(Image.open(io.BytesIO(img1_bytes)).convert('RGB'))
        img2 = np.array(Image.open(io.BytesIO(img2_bytes)).convert('RGB'))

        # Ensure the model name is one of the allowed models
        if model_name not in ['VGG-Face', 'Facenet', 'ArcFace']:
            return jsonify({'error': 'Invalid model name. Choose from VGG-Face, Facenet, ArcFace.'})

        # Perform verification using the specified model
        result = DeepFace.verify(img1_path=img1, img2_path=img2, model_name=model_name)

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

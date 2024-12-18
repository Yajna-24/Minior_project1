from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import json

app = Flask(__name__)

# Load the model and class indices
print("Loading model...")
model = tf.keras.models.load_model('plant_disease_model.h5')

# Load class indices
with open('class_indices.json', 'r') as f:
    class_indices = json.load(f)
    
# Invert class indices for prediction
class_names = {v: k for k, v in class_indices.items()}

def preprocess_image(image):
    # Resize image to match model's expected sizing
    image = image.resize((128, 128))
    # Convert to array and normalize
    img_array = tf.keras.preprocessing.image.img_to_array(image)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
            
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
            
        # Read and preprocess the image
        image_bytes = file.read()
        image = Image.open(io.BytesIO(image_bytes))
        processed_image = preprocess_image(image)
        
        # Make prediction
        predictions = model.predict(processed_image)
        predicted_class_index = np.argmax(predictions[0])
        predicted_class = class_names[predicted_class_index]
        confidence = float(predictions[0][predicted_class_index])
        
        # Format the disease name for display
        disease_name = predicted_class.replace('___', ' - ').replace('_', ' ')
        
        return jsonify({
            'disease': disease_name,
            'confidence': f'{confidence:.2%}'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True)

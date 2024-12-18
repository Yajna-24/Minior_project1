import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import json
import os

def load_and_preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

def predict_disease(model, image_path, class_indices):
    # Load and preprocess the image
    processed_image = load_and_preprocess_image(image_path)
    
    # Make prediction
    predictions = model.predict(processed_image)
    predicted_class_index = np.argmax(predictions[0])
    
    # Get the class name
    class_names = {v: k for k, v in class_indices.items()}
    predicted_class = class_names[predicted_class_index]
    confidence = float(predictions[0][predicted_class_index])
    
    return predicted_class, confidence

def main():
    # Load the model
    model = tf.keras.models.load_model('plant_disease_model.h5')
    
    # Load class indices
    with open('class_indices.json', 'r') as f:
        class_indices = json.load(f)
    
    # Test directory
    test_dir = 'dataset/validation'
    
    print("Testing model predictions...")
    print("-" * 50)
    
    # Test a few images from each class
    for class_name in os.listdir(test_dir):
        class_dir = os.path.join(test_dir, class_name)
        if os.path.isdir(class_dir):
            # Get first image from this class
            images = os.listdir(class_dir)
            if images:
                test_image = os.path.join(class_dir, images[0])
                predicted_class, confidence = predict_disease(model, test_image, class_indices)
                
                print(f"Test image: {test_image}")
                print(f"Actual class: {class_name}")
                print(f"Predicted class: {predicted_class}")
                print(f"Confidence: {confidence:.2%}")
                print("-" * 50)

if __name__ == "__main__":
    main()

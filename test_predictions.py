import os
import requests
from PIL import Image

def test_prediction(image_path):
    """Test the prediction endpoint with an image"""
    try:
        # Open and prepare the image
        with open(image_path, 'rb') as img_file:
            files = {'file': img_file}
            
            # Make the request to our Flask app
            response = requests.post('http://localhost:5000/predict', files=files)
            
            if response.status_code == 200:
                result = response.json()
                print(f"\nResults for {os.path.basename(image_path)}:")
                print(f"Detected Disease: {result['disease']}")
                print(f"Confidence: {result['confidence']}")
                print("-" * 50)
            else:
                print(f"Error: {response.json().get('error', 'Unknown error')}")
                
    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")

def main():
    # Test directory paths
    test_dirs = [
        'dataset/validation/Apple___Apple_scab',
        'dataset/validation/Apple___healthy',
        'dataset/validation/Tomato___Late_blight',
        'dataset/validation/Tomato___healthy'
    ]
    
    print("Starting prediction tests...")
    print("=" * 50)
    
    for test_dir in test_dirs:
        # Get the first image from each category
        try:
            files = os.listdir(test_dir)
            if files:
                image_path = os.path.join(test_dir, files[0])
                test_prediction(image_path)
        except Exception as e:
            print(f"Error accessing directory {test_dir}: {str(e)}")

if __name__ == "__main__":
    main()

import os
import numpy as np
from PIL import Image, ImageDraw
import shutil

def create_test_dataset():
    """Create a small test dataset for immediate use"""
    print("Creating test dataset...")
    
    # Define classes
    classes = [
        'Apple___healthy',
        'Apple___Apple_scab',
        'Tomato___healthy',
        'Tomato___Late_blight',
        'Corn___Common_rust'
    ]
    
    # Create directories
    for split in ['train', 'validation']:
        base_dir = os.path.join('dataset', split)
        os.makedirs(base_dir, exist_ok=True)
        
        for class_name in classes:
            class_dir = os.path.join(base_dir, class_name)
            os.makedirs(class_dir, exist_ok=True)
            
            # Number of images to create
            num_images = 50 if split == 'train' else 10
            
            # Create images for this class
            for i in range(num_images):
                # Create a base image
                img = Image.new('RGB', (224, 224), color='green')
                draw = ImageDraw.Draw(img)
                
                # Add some random patterns based on the class
                if 'healthy' in class_name:
                    color = 'darkgreen'
                else:
                    color = 'brown'
                
                # Draw random shapes
                for _ in range(10):
                    x1 = np.random.randint(0, 224)
                    y1 = np.random.randint(0, 224)
                    x2 = x1 + np.random.randint(10, 50)
                    y2 = y1 + np.random.randint(10, 50)
                    draw.ellipse([x1, y1, x2, y2], fill=color)
                
                # Save the image
                img_path = os.path.join(class_dir, f'image_{i}.jpg')
                img.save(img_path)
                
            print(f"Created {num_images} images for {class_name} in {split} set")
    
    print("Test dataset created successfully!")

if __name__ == "__main__":
    # Clean up existing dataset if any
    if os.path.exists('dataset'):
        shutil.rmtree('dataset')
    
    print("Creating test dataset for immediate use...")
    create_test_dataset()

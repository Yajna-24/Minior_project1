import unittest
from flask import Flask
from PIL import Image
import io
import json
from app import app

class TestPlantDiseaseDetection(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        
        # Create test image
        self.test_image = Image.new('RGB', (128, 128), color='white')
        img_io = io.BytesIO()
        self.test_image.save(img_io, 'JPEG')
        img_io.seek(0)
        self.test_image_data = img_io
    
    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_predict_no_file(self):
        response = self.app.post('/predict')
        self.assertEqual(response.status_code, 400)
    
    def test_predict_empty_file(self):
        response = self.app.post('/predict', data={
            'file': (io.BytesIO(), '')
        })
        self.assertEqual(response.status_code, 400)
    
    def test_predict_invalid_file(self):
        response = self.app.post('/predict', data={
            'file': (io.BytesIO(b'not an image'), 'test.txt')
        })
        self.assertEqual(response.status_code, 500)
    
    def test_predict_valid_image(self):
        response = self.app.post('/predict', data={
            'file': (self.test_image_data, 'test.jpg')
        }, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 200)
        
        # Parse response
        data = json.loads(response.data)
        
        # Check response structure
        self.assertIn('disease', data)
        self.assertIn('confidence', data)
    
    def test_health(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')

if __name__ == '__main__':
    unittest.main()

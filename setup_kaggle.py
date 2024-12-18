import os
import json
from config import KAGGLE_USERNAME, KAGGLE_KEY

def setup_kaggle():
    # Create .kaggle directory
    kaggle_dir = os.path.join(os.path.expanduser('~'), '.kaggle')
    os.makedirs(kaggle_dir, exist_ok=True)
    
    # Create kaggle.json
    kaggle_json = os.path.join(kaggle_dir, 'kaggle.json')
    credentials = {
        "username": KAGGLE_USERNAME,
        "key": KAGGLE_KEY
    }
    
    with open(kaggle_json, 'w') as f:
        json.dump(credentials, f)
    
    # Set permissions
    try:
        os.chmod(kaggle_json, 0o600)
    except:
        pass
    
    print("Kaggle configuration set up successfully!")

if __name__ == "__main__":
    setup_kaggle()

"""
Deployment script for Plant Disease Detection System.
This script helps set up and run the application.
"""

import os
import subprocess
import sys
import json
import shutil
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 7):
        print("Error: Python 3.7 or higher is required")
        sys.exit(1)

def create_directories():
    """Create necessary directories if they don't exist."""
    directories = [
        'static/uploads',
        'static/models',
        'instance',
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {directory}")

def check_requirements():
    """Check if all required packages are installed."""
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'],
                      check=True)
        print("All required packages installed successfully")
    except subprocess.CalledProcessError:
        print("Error: Failed to install required packages")
        sys.exit(1)

def check_model_files():
    """Check if model files exist."""
    required_files = [
        'model.h5',
        'class_indices.json'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("\nWarning: The following model files are missing:")
        for file in missing_files:
            print(f"- {file}")
        print("\nYou need to either:")
        print("1. Run 'python train_model.py' to train a new model")
        print("2. Download pre-trained model files")
        return False
    return True

def setup_database():
    """Set up the SQLite database."""
    try:
        from app import db, app
        with app.app_context():
            db.create_all()
        print("Database setup completed successfully")
    except Exception as e:
        print(f"Error setting up database: {e}")
        sys.exit(1)

def main():
    """Main deployment function."""
    print("Starting deployment process...")
    
    # Check Python version
    check_python_version()
    print("Python version check passed")
    
    # Create necessary directories
    create_directories()
    
    # Check and install requirements
    check_requirements()
    
    # Check model files
    model_exists = check_model_files()
    
    # Setup database
    setup_database()
    
    print("\nDeployment completed!")
    if model_exists:
        print("\nYou can now run the application with:")
        print("python app.py")
    else:
        print("\nBefore running the application, you need to:")
        print("1. Train the model: python train_model.py")
        print("   OR")
        print("2. Download pre-trained model files")
        print("\nThen run: python app.py")

if __name__ == '__main__':
    main()

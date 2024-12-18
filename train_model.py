import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
import json
import os

# Force CPU usage
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# Define constants
IMG_SIZE = 128
BATCH_SIZE = 32
EPOCHS = 50
INITIAL_LR = 0.001

def create_model(num_classes):
    model = Sequential([
        # First Convolutional Block
        Conv2D(32, 3, activation='relu', padding='same', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
        BatchNormalization(),
        Conv2D(32, 3, activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D(),
        Dropout(0.25),
        
        # Second Convolutional Block
        Conv2D(64, 3, activation='relu', padding='same'),
        BatchNormalization(),
        Conv2D(64, 3, activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D(),
        Dropout(0.25),
        
        # Third Convolutional Block
        Conv2D(128, 3, activation='relu', padding='same'),
        BatchNormalization(),
        Conv2D(128, 3, activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D(),
        Dropout(0.25),
        
        # Dense Layers
        Flatten(),
        Dense(512, activation='relu'),
        BatchNormalization(),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])
    
    return model

def prepare_data():
    # Strong data augmentation for training
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=40,
        width_shift_range=0.3,
        height_shift_range=0.3,
        shear_range=0.3,
        zoom_range=0.3,
        horizontal_flip=True,
        vertical_flip=True,
        fill_mode='nearest',
        brightness_range=[0.7, 1.3],
        validation_split=0.2
    )
    
    print("Loading training data...")
    train_generator = train_datagen.flow_from_directory(
        'dataset/train',
        target_size=(IMG_SIZE, IMG_SIZE),
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='training',
        shuffle=True
    )
    
    print("\nLoading validation data...")
    val_generator = train_datagen.flow_from_directory(
        'dataset/train',
        target_size=(IMG_SIZE, IMG_SIZE),
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='validation',
        shuffle=False
    )
    
    # Print and save class indices
    print("\nClass mapping:")
    for class_name, index in train_generator.class_indices.items():
        print(f"{index}: {class_name}")
    
    # Save class indices
    with open('class_indices.json', 'w') as f:
        json.dump(train_generator.class_indices, f, indent=4)
    print("\nSaved class indices to class_indices.json")
    
    return train_generator, val_generator

def train_model():
    # Prepare data
    train_generator, val_generator = prepare_data()
    num_classes = len(train_generator.class_indices)
    print(f"\nNumber of classes: {num_classes}")
    
    # Create and compile model
    print("\nCreating and compiling model...")
    model = create_model(num_classes)
    model.compile(
        optimizer=Adam(learning_rate=INITIAL_LR),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # Add callbacks for better training
    callbacks = [
        EarlyStopping(
            monitor='val_accuracy',
            patience=10,
            restore_best_weights=True
        ),
        ReduceLROnPlateau(
            monitor='val_accuracy',
            factor=0.5,
            patience=5,
            min_lr=1e-6
        )
    ]
    
    # Train model
    print("\nStarting training...")
    history = model.fit(
        train_generator,
        epochs=EPOCHS,
        validation_data=val_generator,
        callbacks=callbacks,
        verbose=1
    )
    
    # Save model
    print("\nSaving model...")
    model.save('plant_disease_model.h5')
    print("Model saved successfully!")
    
    return history

if __name__ == "__main__":
    # Train the model
    history = train_model()

# Fonctions utilitaires pour la partie principale
import cv2
import numpy as np
import tensorflow as tf

MODEL_PATH = 'models/waste_classifier_model.h5'
CLASS_NAMES = ['Plastique', 'Verre', 'Métal', 'Papier', 'Carton', 'Déchet Organique']

# Charger le modèle TensorFlow
model = tf.keras.models.load_model(MODEL_PATH)

def process_image(file):

    # Lire et prétraiter l'image
    file_bytes = np.frombuffer(file.read(), np.uint8)
    print(file_bytes)

    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    image = cv2.resize(image, (224, 224))  # Redimensionner selon les besoins du modèle
    image = image / 255.0  # Normaliser
    image = np.expand_dims(image, axis=0)  # Ajouter une dimension pour le batch

    # Prédiction
    predictions = model.predict(image)
    predicted_class = CLASS_NAMES[np.argmax(predictions)]
    confidence = float(np.max(predictions) * 100)
    
    return predicted_class, confidence
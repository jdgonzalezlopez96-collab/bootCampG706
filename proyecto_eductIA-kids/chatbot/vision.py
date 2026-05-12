import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

# 1. Carga del modelo
model = MobileNetV2(weights='imagenet')

# 2. Diccionarios de mapeo específicos
# Agregamos términos técnicos que la IA suele dar para estos animales
MAPEO_ESPECIFICO = {
    'gato': [
        'tabby', 'tiger_cat', 'persian_cat', 'siamese_cat', 'egyptian_cat', 
        'lynx', 'cat', 'wire-haired_fox_terrier'
    ],
    'caballo': [
        'horse', 'stallion', 'colt', 'sorrel', 'racehorse', 'zebra',
        'flat-coated_retriever'
    ],
    'perrito': [
        'dog', 'puppy', 'beagle', 'english_foxhound', 'walker_hound', 
        'golden_retriever', 'poodle', 'dalmatian', 'pug', 'chihuahua'
    ],
    'marrano': ['hog', 'pig', 'piggy', 'wild_boar'],
    'vaca': [
        'ox', 'cow', 'bull', 'water_buffalo', 'bison', 
        'sorrel' # Se agrega sorrel aquí también porque es el color café que confunde vaca/caballo
    ],
    'oveja': [
        'sheep', 'ram', 'ewe', 'goat', 'angora', 
        'mask', 'wig', 'clothed' # Agregamos términos que la IA asocia a dibujos de ovejas
    ],
    'gallina': ['hen', 'rooster', 'cock', 'cluck', 'chick']
}

def classify_animal(img_path):
    try:
        # A. Preparar la imagen
        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        # B. Predicción (Analizamos el Top 5 para evitar falsos positivos)
        preds = model.predict(x)
        top_results = decode_predictions(preds, top=5)[0]
        
        # Extraemos solo los nombres técnicos detectados
        nombres_detectados = [res[1].lower() for res in top_results]
        
        # C. LÓGICA DE DECISIÓN PRIORITARIA
        # Buscamos de forma EXCLUSIVA en nuestro mapeo antes de dar una respuesta
        animal_final = None
        
        for animal, etiquetas_ia in MAPEO_ESPECIFICO.items():
            # Si cualquiera de las etiquetas técnicas de la IA coincide con nuestro grupo
            if any(etiqueta in nombres_detectados for etiqueta in etiquetas_ia):
                animal_final = animal
                break # Encontró la coincidencia más probable y sale del bucle

        # D. Generación de Respuestas según el animal confirmado
        if animal_final == 'gato':
            return "¡Miau! Es un **gatito** tierno. 🐱 Le gusta jugar y estar en casa."
    
        elif animal_final == 'caballo':
            return "¡Qué elegancia! Es un **caballo** veloz. 🐎 Vive en el campo y es muy fuerte."
    
        elif animal_final == 'marrano':
            return "¡Oink oink! Es un **marranito**. 🐷 Vive feliz en la granja y le gusta el lodo."
    
        elif animal_final == 'vaca':
            return "¡Muu! Es una **vaca**. 🐮 Nos da leche y vive tranquila en el pasto."
    
        elif animal_final == 'oveja':
            return "¡Beeee! Es una **oveja**. 🐑 Su lana es muy suave y calentita."
    
        # NUEVA RESPUESTA
        elif animal_final == 'gallina':
            return "¡Kikirikí! Es una **gallina**. 🐔 Ella pone huevos muy ricos y vive en el gallinero de la granja."

        elif animal_final == 'perrito':
            return "¡Guau guau! Es un **perrito** muy amigable. 🐶 Son los mejores amigos en el hogar."
    
        else:
            # Si no está en nuestra lista principal, intentamos traducir el primer resultado
            primer_resultado = top_results[0][1].replace('_', ' ')
            return f"Parece un {primer_resultado}. 🌍 ¡La naturaleza es asombrosa!"

    except Exception as e:
        print(f"Error: {e}")
        return "¡Uy! Mi visor de animales se distrajo. 📸 ¿Intentamos de nuevo?"
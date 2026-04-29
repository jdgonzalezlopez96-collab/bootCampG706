import os # Trabaja con el sistema operativo para crear o gestionar archivos y directorios
import pickle # Guarda y carga objetos de python en archivos
from sklearn.feature_extraction.text import CountVectorizer
# CountVectorizer convierte texto en un vector
from sklearn.naive_bayes import MultinomialNB
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR,"vectorizer.pkl")
ANSWERS_PATH = os.path.join(MODEL_DIR,"answer.pkl")

# Se crea la función para crear y entrenar el modelo
def build_and_train_model(train_pairs):
    questions = [q for q, _ in train_pairs] # Lista de preguntas
    answers = [a for _, a in train_pairs] # Lista de respuestas
    # Creamos el vectorizador, que traducirá el texto a números
    vectorizer = CountVectorizer()
    # Entrenamos el vectorizados con las preguntas y las respuesta
    # Convertimos en números (Transformamos las preguntas en un vector)
    x = vectorizer.fit_transform(questions)
    # Obtenemos una lista de respuestas únicas (sin repetir)
    unique_answers = sorted(set(answers))
    # Creamos un diccionario que asigne un número a cada respuesta
    # Ejemplo : {"!Hola¡:":0, "!Hasta Luego¡", 1}
    answer_to_label ={a: i for i, a in enumerate(unique_answers)}
    # Creamos una lista con las etiquetas numéricas de las respuestas (Convertimos las respuestas en números)
    # Ejemplo :[0,1,0] según la respuesta correspondiente a cada pregunta
    y = [answer_to_label[a] for a in answers]
    # Creamos el modelo Naive Bayes para clasificación de texto (Creamos el modelo de inteligencia artificial)
    model = MultinomialNB()
    # Entrenamos el modelo con los datos numéricos (preguntas y respuestas)
    model.fit(x,y)
    # Crear carpeta para guardar el modelo si no existe
    os.makedirs(MODEL_DIR,exist_ok=True)
    # Guardar los objetos entrenados
    with open(MODEL_PATH,"wb") as f:
        pickle.dump(model,f)
    with open(VECTORIZER_PATH,"wb") as f:
        pickle.dump(vectorizer,f)
    with open(ANSWERS_PATH,"wb") as f:
        pickle.dump(unique_answers,f)
    print("Ok Modelo entrenado y guardado correctamente")
    return model, vectorizer, unique_answers

def load_model():
    if(
        os.path.exists(MODEL_PATH)
        and os.path.exists(VECTORIZER_PATH)
        and os.path.exists(ANSWERS_PATH)
    ):
        with open(MODEL_PATH,"rb") as f:
            model = pickle.load(f)
        with open(VECTORIZER_PATH,"rb") as f:
            vectorizer = pickle.load(f)
        with open(ANSWERS_PATH, "rb") as f:
            unique_answers = pickle.load(f)
        print("📁 Modelo cargado desde disco.")
        return model, vectorizer, unique_answers
    else:
        print("⚠️ No hay modelo guardado. Será necesario entrenarlo")
        return None, None, None
    
def predict_answer(model, vectorizer, unique_answers, user_text):
    x = vectorizer.transform([user_text])
    label = model.predict(x)[0]
    return unique_answers[label]

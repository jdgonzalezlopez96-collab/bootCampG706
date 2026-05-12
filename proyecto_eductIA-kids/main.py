import os
from flask import Flask, render_template, request, jsonify

# Importamos tus módulos personalizados
from chatbot.model import predict_answer, model, vectorizer, unique_answers
from chatbot.vision import classify_animal

app = Flask(__name__)

# Configuración para la subida de imágenes
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# --- RUTAS DE NAVEGACIÓN ---

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/identificar')
def identificar():
    """Ruta para el laboratorio de animales"""
    return render_template('identificar.html')

@app.route('/aprendizaje')
def aprendizaje():
    return render_template('aprendizaje.html')

@app.route('/beneficios')
def beneficios():
    return render_template('beneficios.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/aprendizaje/<tema>')
def detalle_modulo(tema):
    # Aquí puedes personalizar qué datos enviar según el tema
    datos = {
        'matematicas': {
            'titulo': 'Misión: Matemáticas 🔢',
            'juego1': '/static/juegos/mates/juego1/index.html',
            'juego2': '/static/juegos/mates/juego2/index.html'
        },
        'ingles': {
            'titulo': 'Misión: English Adventure 🇬🇧',
            'juego1': '/static/juegos/ingles/juego1/index.html',
            'juego2': '/static/juegos/ingles/juego2/index.html'
        },
        'espanol': {
            'titulo': 'Misión: Español',
            'juego1': '/static/juegos/espanol/juego1/index.html',
            'juego2': '/static/juegos/espanol/juego2/index.html'
        },
        'etica': {
            'titulo': 'Misión: Ética',
            'juego1': '/static/juegos/etica/juego1/index.html'
        },
        'deporte': {
            'titulo': 'Misión: Deporte',
            'juego1': '/static/juegos/deporte/juego1/index.html'
        },
        'programacion': {
            'titulo': 'Misión: Programación',
            'juego1': '/static/juegos/programacion/juego1/index.html',
            'juego2': '/static/juegos/programacion/juego2/index.html'
        }
    }
    
    # Obtenemos la información del tema seleccionado
    info = datos.get(tema)
    
    return render_template('modulo_detalle.html', info=info)




# --- RUTAS DE INTELIGENCIA ARTIFICIAL ---

@app.route('/chat', methods=['POST'])
def chat():
    user_text = request.form.get("message", "").lower()
    
    # 1. Filtro de Seguridad: Si el niño habla de sentimientos, bloqueamos el código técnico
    sentimientos_detectados = {
        "feliz": ["feliz", "bien", "alegre", "genial", "divertido", "me gusta", "wow"],
        "triste": ["triste", "mal", "aburrido", "dificil", "no puedo", "ayuda", "feo"]
    }

    # Si detectamos una palabra emocional, respondemos con el corazón y NO con el modelo técnico
    for emocion, palabras in sentimientos_detectados.items():
        if any(p in user_text for p in palabras):
            if emocion == "feliz":
                return jsonify({"response": "¡Qué increíble! Me pone muy feliz que estés disfrutando tu aprendizaje. ✨ ¿Qué más quieres descubrir?"})
            else:
                return jsonify({"response": "Entiendo... a veces aprender cosas nuevas es un reto, pero ¡tú eres muy valiente! 😊 ¿Quieres que intentemos algo más fácil?"})

    # 2. Si no hay sentimientos claros, usamos el modelo pero con un "traductor" amigable
    try:
        respuesta_tecnica = predict_answer(model, vectorizer, unique_answers, user_text)
        
        # Si la respuesta del modelo suena a "programación" o "código", la traducimos para el niño
        if "código" in respuesta_tecnica or "programar" in respuesta_tecnica:
            return jsonify({"response": "¡Eso suena a magia de computadoras! 💻 Pero hoy estamos aprendiendo sobre animales y diversión. ¿Quieres ver otra foto?"})
            
        return jsonify({"response": respuesta_tecnica})
    except:
        return jsonify({"response": "¡Ups! Mi cerebrito de robot hizo corto circuito. 🤖 ¿Me lo repites más sencillo?"})


@app.route('/predict_animal', methods=['POST'])
def predict_animal():
    """
    Recibe la imagen desde el laboratorio, la procesa con TensorFlow
    y devuelve la clasificación amigable.
    """
    if 'file' not in request.files:
        return jsonify({"error": "No se subió ninguna imagen"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Nombre de archivo vacío"}), 400

    # Guardar archivo temporalmente
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    
    try:
        # Llamamos a la función mágica de vision.py
        resultado = classify_animal(filepath)
        return jsonify({
            "prediction": resultado, 
            "image_path": filepath
        })
    except Exception as e:
        print(f"Error en visión: {e}")
        return jsonify({"prediction": "¡Uy! Mi visor de animales falló. ¿Intentamos con otra foto?"}), 500

# --- INICIO DE LA APLICACIÓN ---

if __name__ == '__main__':
    # Ejecutamos en modo debug para ver cambios en tiempo real
    app.run(debug=True, port=5000)
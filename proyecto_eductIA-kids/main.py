from flask import Flask, render_template, request, jsonify
from chatbot.data import training_data
from chatbot.model import build_and_train_model, load_model, predict_answer
app = Flask(__name__)

# Cargar el modelo una sola vez al iniciar el servidor
model, vectorizer, unique_answers = load_model()
if model is None:
    model, vectorizer, unique_answers = build_and_train_model(training_data)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/beneficios')
def beneficios():
    return render_template('beneficios.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/aprendizaje')
def aprendizaje():
    return render_template('aprendizaje.html')

@app.route('/mapa')
def mapa():
    return render_template('mapa.html')

@app.route('/chat', methods=['POST'])
def chat():
    # Recibimos el mensaje desde el fetch de JavaScript
    user_text = request.form.get("message","")
    if not user_text.strip():
        return jsonify({"response":"Por favor escribe algo 😁"})
    response = predict_answer(model,vectorizer,unique_answers,user_text)
    return jsonify({"response": response})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
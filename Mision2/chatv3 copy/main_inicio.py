from flask import Flask, render_template, request, jsonify
from chatbot.data import training_data
from chatbot.model import build_and_train_model, load_model, predict_answer

app = Flask(__name__)

# Cargar el modelo una sola vez al iniciar el servidor
model, vectorizer, unique_answers = load_model()
if model is None:
    model, vectorizer, unique_answers = build_and_train_model(training_data)

@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/ask', methods=['POST'])
def ask():
    # Recibimos el mensaje desde el fetch de JavaScript
    user_message = request.json.get("mensaje").strip()
    
    if not user_message:
        return jsonify({"respuesta": "Escribe algo válido."})

    # Usamos tu función de predicción existente
    response = predict_answer(model, vectorizer, unique_answers, user_message)
    
    return jsonify({"respuesta": response})

if __name__ == "__main__":
    app.run(debug=True)
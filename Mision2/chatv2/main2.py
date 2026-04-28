from chatbot.data import training_data
from chatbot.model import build_and_train_model, load_model, predict_answer
def chat(model,vectorizer,unique_answers):
    """Inicia el modo de conversación"""
    print("\n 🤖 Chatbot listo. Escribe 'salir' para terminar. \n")
    while True:
        user = input("Tú: ").strip()
        if user.lower() in {"salir","exit","quit"}:
            print("bot: !Hasta pronto¡")
            break
        response = predict_answer(model,vectorizer,unique_answers,user)
        print("Bot: ", response)

def main():
    model, vectorizer, unique_answers = load_model()
    # Menú principal
    while True:
        print("\n=== 🤖 MENÚ PRINCIPAL DEL CHATBOT 🤖 ===")
        print("1️⃣ Chatear con el modelo")
        print("2️⃣ Reentrenar el modelo ")
        print("3️⃣ Salir ")
        opcion=input("\n Elige una opción (1-3); ").strip()
        if opcion == "1":
            if model is None:
                print("\n ⚠️ No hay modelo entrenado. Entrénelo primero.")
            else:
                chat(model,vectorizer,unique_answers)
        elif opcion == "2":
            print("\n 🔁 Reentrenar el modelo con los nuevos datos...")
            model,vectorizer,unique_answers=build_and_train_model(training_data)
            print("✅ Modelo actualizado correctamente.")
        elif opcion == "3":
            print("\n 👋 ¡Hasta luego!")
            break
        else:
            print("\n ✖️ Opción no válida. Intenta nuevamente.")
if __name__== "__main__":
    main()
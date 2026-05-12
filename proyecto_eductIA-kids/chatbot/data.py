training_data = [
    # Saludos básicos
    ("hola", "¡Hola! Soy tu asistente de EducatIA. Por favor, elige qué quieres aprender hoy escribiendo el número:\n1. Matemáticas\n2. Inglés\n3. Educación Física\n4. Español\n5. Ética\n6. Programación\n7. Identificar Animales"),
    
    # Opciones numéricas con rutas
    ("1", "¡Genial! Vamos a aprender Matemáticas Básicas. Haz clic aquí: /aprendizaje"),
    ("2", "¡Perfecto! El inglés es muy importante. Ir a: /aprendizaje"),
    ("3", "¡A mover el cuerpo! Vamos a Educación Física: /aprendizaje"),
    ("4", "Excelente, aprenderemos Español: /aprendizaje"),
    ("5", "La ética y los valores son fundamentales: /aprendizaje"),
    ("6", "¡Futuro programador! Vamos a la clase: /aprendizaje"),
    ("7", "¡Genial! Vamos al laboratorio de animales. Haz clic aquí: /identificar"),
    
    
    # También incluimos las variaciones por nombre por si el usuario escribe el texto
    ("matematicas", "Claro, aquí tienes el módulo de Matemáticas: /aprendizaje"),
    ("ingles", "Ready? Vamos a Inglés: /aprendizaje"),
    ("Educación Física", "listo? para ejercitarse, vamos a Educación Física: /aprendizaje"),
    ("Español", "Conozcamos a HELE Vamos a Español: /aprendizaje"),
    ("ética", "Vamos a ética y valores: /aprendizaje"),
    ("programación", "A tirar código!!! Vamos a programación básica: /aprendizaje"),
    ("identificar animales", "Claro, vamos a identificar animales aquí: /identificar"),
    ("descubrir animales", "¡Perfecto! Vamos a descubrir animales en: /identificar")
]

# Datos para detectar la emoción del niño
sentiment_data = [
    # FELIZ / POSITIVO
    ("estoy feliz", "positivo"), ("que divertido", "positivo"), ("me gusta", "positivo"),
    ("estoy bien", "positivo"), ("genial", "positivo"), ("super", "positivo"),
    # TRISTE / FRUSTRADO
    ("estoy triste", "negativo"), ("no entiendo", "negativo"), ("es dificil", "negativo"),
    ("me rindo", "negativo"), ("no puedo", "negativo"), ("estoy aburrido", "negativo")
]

# Respuestas especiales según el sentimiento
sentiment_responses = {
    "positivo": "¡Me encanta ver que te diviertes! 🌟 ¡Sigamos aprendiendo!",
    "negativo": "¡No te preocupes! 😊 A veces aprender cosas nuevas toma tiempo. ¿Quieres intentar algo más fácil o que te lo explique de otra forma?"
}
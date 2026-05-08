training_data = [
    # Saludos básicos
    ("hola", "¡Hola! Soy tu asistente de EducatIA. Por favor, elige qué quieres aprender hoy escribiendo el número:\n1. Matemáticas\n2. Inglés\n3. Educación Física\n4. Español\n5. Ética\n6. Programación"),
    
    # Opciones numéricas con rutas
    ("1", "¡Genial! Vamos a aprender Matemáticas Básicas. Haz clic aquí: /templates/aprendizaje"),
    ("2", "¡Perfecto! El inglés es muy importante. Ir a: /templates/aprendizaje"),
    ("3", "¡A mover el cuerpo! Vamos a Educación Física: /templates/aprendizaje"),
    ("4", "Excelente, aprenderemos Español: /templates/aprendizaje"),
    ("5", "La ética y los valores son fundamentales: /aprendizaje"),
    ("6", "¡Futuro programador! Vamos a la clase: /templates/aprendizaje"),
    
    # También incluimos las variaciones por nombre por si el usuario escribe el texto
    ("matematicas", "Claro, aquí tienes el módulo de Matemáticas: /templates/aprendizaje"),
    ("ingles", "Ready? Vamos a Inglés: /templates/aprendizaje"),
    ("Educación Física", "listo? para ejercitarse, vamos a Educación Física: /templates/aprendizaje"),
    ("Español", "Conozcamos a HELE Vamos a Español: /templates/aprendizaje"),
    ("ética", "Vamos a ética y valores: /templates/aprendizaje"),
    ("programación", "A tirar código!!! Vamos a programación básica: /templates/aprendizaje")
]
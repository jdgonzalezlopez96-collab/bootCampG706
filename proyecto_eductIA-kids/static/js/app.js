const form = document.getElementById("chatForm");
const input = document.getElementById("userInput");
const messages = document.getElementById("messages");
const chatWrapper = document.getElementById("chat-wrapper");

// 1. Función para procesar y mostrar mensajes del Bot (con soporte de enlaces)
function appendBotMessage(text) {
    let botResponse = text;
    
    // Lógica para convertir la ruta (ej: /aprendizaje) en un enlace real
    // Buscamos cualquier palabra que empiece con /
    const urlMatch = botResponse.match(/\/[a-z0-9]+/); 
    
    if (urlMatch) {
        const url = urlMatch[0];
        botResponse = botResponse.replace(url, `<a href="${url}" style="color: #007bff; font-weight: bold; text-decoration: underline;">¡Haz clic aquí para ir!</a>`);
    }

    messages.innerHTML += `<div class="msg bot"><b>Bot:</b> ${botResponse}</div>`;
    messages.scrollTop = messages.scrollHeight;
}

// 2. Manejo del envío del formulario
form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const text = input.value.trim();
    if (!text) return;

    // Mostrar mensaje del usuario
    messages.innerHTML += `<div class="msg user"><b>Tú:</b> ${text}</div>`;
    input.value = "";

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: `message=${encodeURIComponent(text)}`
        });

        const data = await response.json();
        appendBotMessage(data.response);
    } catch (error) {
        console.error("Error en el chat:", error);
    }
});

// 3. Despliegue automático a los 4 segundos
window.addEventListener('load', () => {
    setTimeout(() => {
        // Mostramos el chat
        chatWrapper.style.display = "flex";
        
        // Mensaje de bienvenida automático con opciones
        const welcomeText = "¡Hola! ¿Qué quieres aprender hoy? 😊 Escribe el número:<br>1. Matemáticas Básicas<br>2. Inglés básico<br>3. Educación física y deporte";
        appendBotMessage(welcomeText);
    }, 4000);
});
const form = document.getElementById("chatForm");
const input = document.getElementById("userInput");
const messages = document.getElementById("messages");
const chatWrapper = document.getElementById("chat-wrapper");
const chatClose = document.getElementById("chat-close"); // Nuevo
const chatToggle = document.getElementById("chat-toggle"); // Nuevo

// --- FUNCIONES DE CONTROL ---

function openChat() {
    chatWrapper.style.display = "flex";
}

function closeChat() {
    chatWrapper.style.display = "none";
}

// Eventos para abrir y cerrar
chatToggle.addEventListener("click", openChat);
chatClose.addEventListener("click", closeChat);

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

// 3. Despliegue automático a los 4 segundos con la lógica de saludo según la ruta
window.addEventListener('load', () => {
    setTimeout(() => {
        // Mostramos el chat
        chatWrapper.style.display = "flex";
        
        // Mensaje de bienvenida automático con opciones
        const path = window.location.pathname;
        let welcomeText = "";

        if (path === "/" || path === "/index") {
            // Solo en el Index muestra las opciones
            welcomeText = "¡Hola! ¿Qué quieres aprender hoy? 😊 Escribe el número:<br>1. Matemáticas Básicas<br>2. Inglés básico<br>3. Educación física y deporte<br>4. Español<br>5. ética y valores<br>6. Programación Básica<br>7. Identificar Animales 🐶";
        } 
        else if (path === "/identificar") {
            welcomeText = "¡Estás en el Laboratorio de Animales! 🐾 Aquí puedes cargar o arrastrar una foto para saber qué animal es. ¿Cómo te sientes hoy explorando la naturaleza?";
        }
        else if (path === "/aprendizaje") {
            welcomeText = "¡Bienvenido a la zona de estudio! 📚 Aquí verás todos tus módulos. ¿Hay alguna materia que te haga sentir muy feliz hoy?";
        }
        else if (path === "/beneficios") {
            welcomeText = "¡Mira todo lo que puedes lograr! 🚀 ¿Te sientes emocionado por aprender cosas nuevas?";
        }
        else {
            // Saludo general para otras rutas
            welcomeText = "¡Hola! Ya estás en esta sección. Cuéntame, ¿cómo te va en tu aventura de hoy?";
        }

        appendBotMessage(welcomeText);
    }, 4000);
});


function abrirJuego(ruta) {
    console.log("Intentando abrir el juego en:", ruta);
    const modal = document.getElementById('gameModal');
    const frame = document.getElementById('gameFrame');
    
    if (modal && frame) {
        // Usamos style.cssText para asegurarnos de que se aplique el display
        modal.style.cssText = "display: flex !important; visibility: visible !important;";
        frame.src = ruta;
    } else {
        console.error("No se encontró el modal o el frame en el HTML");
    }
}


function cerrarJuego() {
    const modal = document.getElementById('gameModal');
    const frame = document.getElementById('gameFrame');
    
    modal.style.display = 'none';
    frame.src = "";
}

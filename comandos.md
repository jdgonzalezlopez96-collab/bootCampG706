# Comandos
1. **Comandos Git**  
📝 `git --version` -> Me sirve para consultar la version del git  
`cd` -> Me sirve para navegar entre carpetas  
`cd ..` -> Para devolverme una carpeta  
`git init` -> Para inicializar el repositorio vacío  
`git status` -> Para verificar estado de archivos  
`git add .` -> para agregar los archivos a mi git (caja)  
`git commit -m "first commit"` -> para sellar la caja y colocarle un comentario  
`git config --global user.email "jdgonzalezlopez96@gmail.com"` -> Configurarle el correo  
`git config --global user.name "Jhon Daniel Gonzalez Lopez"` -> Configurarle el nombre  
`git remote add origin https://github.com/jdgonzalezlopez96-collab/bootCampG706.git` -> Agrego la ruta origen del repositorio git mío  
`git push -u origin master` -> Le envío o empujo los cambios que yo tengo local en mi equipo al repositorio de github  
`git clone https://github.com/fernandogallegoh75/BootCampProfesG706.git` -> Para clonar un repositorio (en este caso me clonpe el de los profes) 
``git remote -v`` -> verificar la ruta del github a la que se está apuntando

`Set-ExecutionPolicy Unrestricted` -> Se debe ejecutar dentro del powershell como administrador y sirve para habilitar ejecución de comandos

``Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser`` -> Se debe ejecutar dentro del powershell como administrador y sirve para habilitar ejecución de comandos cuando arroja error en el powershell

`dir` -> consultar el directorio donde estoy ubicado y el directorio próximo

``alt + shift + a`` -> comentario en bloque para HTML
``alt + flechita arriba o abajo`` -> Para subir o bajar de posición algo que se aya escrito parándose al final de la línea
``alt + shift + flecha arriba o abajo`` -> copia un bloque de codigo seleccionado abajo o arriba
``alt + flecha arriba o abajo`` -> mueve un bloque de código hacia arriba respetando la identación
``shift + alt + f`` -> Para formatear o identar el código seleccionado

`python --version` -> Consultar versión de python.  
`python -m venv env312` -> crear un entorno virtual en python.  
``env312\Scripts\activate`` -> Activar el entorno virtual de python.  
``deactivate` `-> desactiva el entorno virtual de python cuando no se va a utilizar.  
``pip list`` -> Permite ver las librerías que tiene python.
## Librerias para python
``python.exe -m pip install --upgrade pip`` -> Actualiza el pip
``pip install pandas numpy matplolib`` ->
``pandas`` -> Manejo de datos ``pip install pandas``
``numpy`` -> cálculo matemático ``pip install numpy``
``matplolib`` -> gráficos ``pip install matplolib``

``pip freeze > requirements.txt`` -> Sacar lista de versiones con la que se construyó la aplicación en python

## En caso que se vaya a clonar el proyecto desde el github en cualquier otro equipo y que este a su vez funcione correctamente con las versiones de las librerías correspondioentes al proyecto con las que se construyó.
`python -m venv env312` -> creamos el entorno virtual en python dentro del directorio Mision2.
``env312\Scripts\activate``  -> Activar el entorno virtual de python dentro del directorio Mision2.
``pip freeze > requirements.txt`` -> Se crea archivo requirements para sacar lista de versiones con la que se construyó la aplicación en python dentro del directorio Mision2/chatv1
``pip install -r requirements.txt`` -> Se instala todas las librerías que componen al proyecto hecho en python
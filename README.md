# bot-telegram

https://python-telegram-bot.org/

## Requisitos Previos

Tener instalado Python 3 o superior en tu sistema.
Contar con acceso a internet para instalar las dependencias.
Tener una cuenta de Telegram y haber creado un bot utilizando BotFather. Guarda el token de tu bot para configurarlo más adelante.

### Crear un entorno virtual

python3 -m venv .venv

### Activar entorno virtual

   (Linux o MacOs)

source .venv/bin/activate

   (Windows)

.venv\Scripts\activate

### Para desactivar el entorno virtual, utiliza:

deactivate 

### Intalar las Dependencias:

asegurate de estar dentro del entorno virtual
instalar dependencias que estar en el archivo requirements.txt

pip install -r requirements.txt

### Comando para Actualizar el archivo requirements.txt(Opcional)
pip freeze> requirements.txt

## Ngrok  ¿Qué es ngrok y por qué lo utilizamos?

ngrok es una herramienta que crea un túnel seguro desde tu máquina local a Internet. Esto nos permite:

Probar el bot de Telegram en desarrollo sin necesidad de desplegarlo en un servidor en producción.
Recibir actualizaciones de Telegram (webhooks) a través de una URL pública HTTPS.
Ahorrar tiempo y recursos al no requerir servidores adicionales durante el desarrollo.

#### ¿Cómo funciona en este proyecto?

ngrok expone el puerto 80 de tu máquina local a una URL pública.

La URL generada es configurada automáticamente como el webhook del bot de Telegram.
Telegram envía las actualizaciones del bot (mensajes, comandos, etc.) a la URL pública proporcionada por ngrok.

El bot las procesa y responde según lo programado.


Proporciona una URL pública temporal (HTTPS), enlazada a tu servidor local.
Telegram utiliza esta URL para enviar las actualizaciones.
Facilita el desarrollo y prueba de bots sin necesidad de desplegar un servidor en producción.
Ejemplo de README.md
markdown
Copiar código
# Bot de Telegram con Flask y `ngrok`

Este proyecto es un bot de Telegram desarrollado con Flask, que utiliza `ngrok` para exponer el servidor local y recibir actualizaciones a través de webhooks.



<p align="left">
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://icon.icepanel.io/Technology/png-shadow-512/Flask.png" alt="flask" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

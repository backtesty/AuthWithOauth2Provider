# Autenticación con Google, Github y LinkedIn en Django

<!-- ABOUT THE PROJECT -->
## Acerca del proyecto

Este proyecto que implementa la autenticación mediante el protocolo OAuth2 en Django.
Sin usar paquetes de terceros, se muestra cómo autenticar usuarios con Google, Github y LinkedIn en Django.
También se muestra cómo obtener información del usuario autenticado.

## Tutorial
* Vídeo tutorial de Youtube <a href="https://youtu.be/RT-Jt7edI44">https://youtu.be/RT-Jt7edI44</a>
 
<!-- GETTING STARTED -->
## Tecnologías

* Python
* Django
* requests (librería de Python)
* requests_oauthlib (librería de Python)

### Prerequisitos

Debe tener instalado Python en su computadora. Puede descargarlo desde el siguiente enlace: <a href="https://www.python.org/downloads/">https://www.python.org/downloads/</a>

* Clonar el repositorio
  ```sh
  git clone https://github.com/backtesty/AuthWithOauth2Provider.git
  ```

* Crear el entorno virtual
  ```sh
  python -m venv env
  ```
* Activar entorno virtual (windows):
  ```sh
  env\Scripts\activate
  ```
* Instalar las dependencias del proyecto:
  ```sh
  pip install -r requirements.txt
  ```
* Migrar la base de datos:
  ```sh
  python manage.py migrate
  ```
* Crear un superusuario:
  ```sh
  python manage.py createsuperuser
  ```
* Ejecutar el servidor:
  ```sh
  python manage.py runserver 5000
  ```
## Configuración de las credenciales de OAuth2 [Client ID y Client Secret key]

### Google
* Crear un proyecto en Google Cloud Platform: <a href="https://console.cloud.google.com/">https://console.cloud.google.com/</a>

### Github
* Crear una aplicación en Github: <a href="https://github.com/settings/developers">https://github.com/settings/developers</a>

### LinkedIn
* Crear una aplicación en LinkedIn: <a href="https://www.linkedin.com/developers/apps">https://www.linkedin.com/developers/apps</a>

## Finalmente

Agradezco tu visita, no olvides seguirme y tu respectivo me gusta si te sirvió el vídeo, más información en mi canal de <a href="https://www.youtube.com/channel/UCxGqlLmQXjFjkrnSRLa7B7g">YouTube</a>.
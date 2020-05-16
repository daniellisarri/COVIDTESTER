# COVIDTESTER

_Proyecto de aplicación web apra la rápida detección de contagios por COVID-19 y recogida de datos para su posterior estudio._


### Pre-requisitos 📋
_Requisitos necesarios para ver los avances del proyecto._

+ Para poder ver los avances de este proyecto necesitas, en cuanto a hardware:
    - Al menos 1GB de espacio libre en disco.
    - Procesador Intel Atom/Core I3 o superior.
    - Sistema operativo Windows.
+ En cuanto a software instalado en el sistema:
    - Python 3.8.2.
    - Git.

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

+ Para poder utilizar la aplicación en nuestro sistema, debemos clonarlo antes, utilizando la consola de Windos y siguiendo estos pasos:
    1. Desde la carpeta que estemos utilizando como repertorio local, hacemos 'click derecho+Shift' -> "Abrir la ventana de Power Shell aquí". Se nos abrirá la consola de comandos.
    2. (Sólo una vez) Debemos definir esta carpeta como nuestro repositorio local con el siguiente comando:
        ```
        $ git init
        ```
    3. (Sólo una vez) Una vez definido el repositorio local, debemos indicar el repositorio remoto con el siguiente comando:
        ```
        $ git remote add origin https://github.com/daniellisarri/COVIDTESTER.git 
        ```
    4. Finalmente, para copiar el repositorio remoto a nuestra carpeta introducimos el siguiente comando:
        ```
        $ git pull origin master
        ```
- De esta manera, ya tenemos todo el proyecto en nuestro repositorio local. Si quisieramos actualizarlo, sólo debemos reazliar los pasos 1 y 4.

Mira **Deployment** para conocer como desplegar el proyecto.

## Despliegue 📦

_Con estas instrucciones podrás desplegar la aplicación en tu PC para ver su ejecución._

+ Para lanzar la aplicación se deben seguir estas instrucciones:
    1. Desde la carpeta que estemos utilizando como repertorio local, hacemos 'click derecho+Shift' -> "Abrir la ventana de Power Shell aquí". Se nos abrirá la consola de comandos.
    2. Debemos movernos al mismo nivel en el que se encuentra el archivo "manage.py" mediante el siguiente comando:
        ```
        $ cd .\COVIDTESTER\
        ```
    3. Desde aquí, lanzamos el servidor con el siguiente comando:
        ```
        $ python .\manage.py runserver
        ```
    4. Ya tenemos el servidor en marcha. Para ver la página web debemos introducir en nuestro navegador preferido la siguiente dirección: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Andrés Villanueva** - *Trabajo Inicial* - [villanuevand](https://github.com/villanuevand)
* **Fulanito Detal** - *Documentación* - [fulanitodetal](#fulanito-de-tal)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* etc.



---
⌨️ con ❤️ por [Villanuevand](https://github.com/Villanuevand) 😊


=======

_Requisitos necesarios para ver los avances del proyecto._

+ Para poder ver los avances de este proyecto necesitas, en cuanto a hardware:
    - Al menos 1GB de espacio libre en disco.
    - Procesador Intel Atom/Core I3 o superior.
    - Sistema operativo Windows.
+ En cuanto a software instalado en el sistema:
    - Python 3.8.2.
    - Git.

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

+ Para poder utilizar la aplicación en nuestro sistema, debemos clonarlo antes, utilizando la consola de Windos y siguiendo estos pasos:
    1. Desde la carpeta que estemos utilizando como repertorio local, hacemos 'click derecho+Shift' -> "Abrir la ventana de Power Shell aquí". Se nos abrirá la consola de comandos.
    2. (Sólo una vez) Debemos definir esta carpeta como nuestro repositorio local con el siguiente comando:
        ```
        $ git init
        ```
    3. (Sólo una vez) Una vez definido el repositorio local, debemos indicar el repositorio remoto con el siguiente comando:
        ```
        $ git remote add origin https://github.com/daniellisarri/COVIDTESTER.git 
        ```
    4. Finalmente, para copiar el repositorio remoto a nuestra carpeta introducimos el siguiente comando:
        ```
        $ git pull origin master
        ```
- De esta manera, ya tenemos todo el proyecto en nuestro repositorio local. Si quisieramos actualizarlo, sólo debemos reazliar los pasos 1 y 4.

Mira **Despliegue** para conocer como desplegar el proyecto.

### Ajustes de instalación 🔧

_Ajustes necesarios para desplegar la aplicación en cada PC_

+ Antes de intentar desplegar la app debemos cambiar algunas líneas de código en el archivo "settings.py". Este archivo se encuentra en "Repo_Local/COVIDTESTER/COVIDTESTER/settings.py". Podemos abrirlo con el IDE de nuestra preferencia:
    1. En la línea 30, debemos definir la locaclización de nuestro directorio estático. Este se encuentra en "Repo_Local/COVIDTESTER/AutoTest/static". Copiamos su localización absoluta y lo indicamos en el archivo. Debe quedar así:
    ```
    STATICFILES_DIRS = [ # Directorio estático
        "C:/..../Repo_Local/COVIDTESTER/AutoTest/static",
    ]
    ```
    2. De manera similar, en la línea 60, debemos definir la locaclización de nuestro directorio de plantillas. Este se encuentra en "Repo_Local/COVIDTESTER/AutoTest/templates". Copiamos su localización absoluta y lo indicamos en el archivo. Debe quedar así:
    ```
    'DIRS': ["C:/..../Repo_Local/COVIDTESTER/AutoTest/templates"],
    ```
- Tras hacer estos cambios, estamos listos para desplegar la aplicación.

## Despliegue 📦

_Con estas instrucciones podrás desplegar la aplicación en tu PC para ver su ejecución. Debemos haber leido antes **Ajustes de instalación**_

+ Para lanzar la aplicación se deben seguir estas instrucciones:
    1. Desde la carpeta que estemos utilizando como repertorio local, hacemos 'click derecho+Shift' -> "Abrir la ventana de Power Shell aquí". Se nos abrirá la consola de comandos.
    2. Debemos movernos al mismo nivel en el que se encuentra el archivo "manage.py" mediante el siguiente comando:
        ```
        $ cd .\COVIDTESTER\
        ```
    3. Desde aquí, lanzamos el servidor con el siguiente comando:
        ```
        $ python .\manage.py runserver
        ```
    4. Ya tenemos el servidor en marcha. Para ver la página web debemos introducir en nuestro navegador preferido la siguiente dirección: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    5. Cuando queramos apagar el servidor, sobre la consola de comandos hacemos click en las teclas 'Ctrl+C'.

## Construido con 🛠️

_Herramientas utilizadas para el desarrollo de este proyecto_

* [Python 3.8.2.](https://www.python.org/) - Lenguaje de programación.
* [DJango 3.0.6](https://www.djangoproject.com/) - El framework web usado.
* [SQLite 3.31.1](https://www.sqlite.org/index.html) - Sistema gestor de base de datos.
* [PyCharm Community](https://www.jetbrains.com/es-es/pycharm/)/[VSC](https://code.visualstudio.com/) - Entornos de desarrollo integados.

## Versionado 📌

Usamos [GIT](https://git-scm.com/) como software de control de versiones. El repositorio remoto se encuentra en [GitHub](https://github.com/daniellisarri/COVIDTESTER).

## Autores ✒️

* **Jon Beloki** - *Gestión de bases de datos*
* **Javier Calzada** - *Lógica de funcionamiento*
* **Daniel Lisarri** - *Interfaz gráfica y de usuario*

También puedes mirar la lista de todos los [contribuyentes](https://github.com/daniellisarri/COVIDTESTER/graphs/contributors) quíenes han participado en este proyecto. 
>>>>>>> 607656f12282272ddee7de3829c99c07bbb24ec4

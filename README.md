

# 📞 Agenda Flask App

Una sencilla aplicación web de agenda desarrollada con Flask y SQLite para gestionar contactos. Permite añadir, visualizar, y gestionar información de contactos (nombre, teléfono, email).

## ✨ Características

* **Gestión de Contactos:** Añade, visualiza, edita y elimina contactos.
* **Persistencia de Datos:** Los contactos se almacenan de forma persistente en una base de datos SQLite.
* **Interfaz Web:** Accede a la agenda a través de un navegador web.
* **Tecnologías:** Desarrollada con Python (Flask) y SQLite para la base de datos.

## 🚀 Tecnologías Utilizadas

* **Python 3.x**
* **Flask:** Micro-framework web para Python.
* **SQLite3:** Base de datos ligera embebida.

## 🛠️ Instalación y Configuración

Sigue estos pasos para poner en marcha el proyecto en tu máquina local.

### 1. Clonar el Repositorio (ejemplo, ajusta si tu repo es diferente)

```bash
git clone [https://github.com/Diony-dev/Agenda-flask.git](https://github.com/Diony-dev/Agenda-flask.git)
cd Agenda-flask
```
*(Nota: Si tu repositorio tiene otro nombre o es privado, ajusta el comando `git clone`.)*

### 2. Crear y Activar un Entorno Virtual

Es una buena práctica utilizar entornos virtuales para gestionar las dependencias de Python.

```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows:
.\venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

### 3. Instalar Dependencias

Una vez activado el entorno virtual, instala las librerías necesarias:

```bash
pip install Flask
# sqlite3 viene integrado con Python, no necesita instalación adicional.
```

### 4. Estructura de Archivos (Esperada)

Asegúrate de que tu proyecto tenga una estructura similar a esta:

```
Agenda-flask/
├── app.py              # La aplicación principal de Flask
├── pydb.py             # Clase para interactuar con la base de datos SQLite
├── contacto.py         # Clase Contacto y la clase Agenda (opcional si solo usas la DB)
├── templates/
│   ├── index.html      # Plantilla principal para mostrar contactos
│   └── registro.html   # Plantilla para añadir nuevos contactos
└── agenda.db           # Archivo de la base de datos SQLite (se creará automáticamente)
```

### 5. Ejecutar la Aplicación

Con el entorno virtual activado, puedes iniciar la aplicación Flask:

```bash
flask run
```

O, si estás usando el `if __name__ == '__main__':` en `app.py`:

```bash
python app.py
```

La aplicación se ejecutará en `http://127.0.0.1:5000/` (o un puerto similar).

## 🚀 Uso de la Aplicación

1.  **Abrir en el Navegador:** Abre tu navegador web y navega a `http://127.0.0.1:5000/`.
2.  **Ver Contactos:** La página principal (`/`) mostrará la lista de contactos existentes en la base de datos.
3.  **Añadir Contactos:** Haz clic en el enlace o botón que te lleve a `/add` (generalmente asociado a `registro.html`) para rellenar el formulario y añadir un nuevo contacto.
4.  **Actualizar/Eliminar:** Si implementas rutas para actualizar o eliminar contactos (lo cual no está en el `app.py` proporcionado pero tu `PyDB` sí soporta), podrás interactuar con ellas desde la interfaz.

## 📝 Notas sobre la Conexión a la Base de Datos

El archivo `pydb.py` gestiona la conexión a la base de datos SQLite. Es importante destacar que, para aplicaciones Flask en producción que manejan múltiples solicitudes simultáneamente, se recomienda una estrategia de gestión de conexiones por solicitud (utilizando `g` y `teardown_appcontext` de Flask) en lugar de una conexión global, para evitar problemas de concurrencia y fugas de recursos. La implementación actual es adecuada para el desarrollo y aplicaciones de pequeña escala.

## 📄 Licencia

Este proyecto está bajo la licencia [Ej: MIT License / Apache 2.0 License].
*(Añade aquí la licencia que elijas para tu proyecto.)*

## 🧑‍💻 Autor

[Tu Nombre o Nombre de Usuario en GitHub] - [Tu Email o Perfil de GitHub]

---
```

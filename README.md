# Cloud Inhouse & Infrastructure
# To-Do List App

Este proyecto es una aplicación de **To-Do List** desarrollada en **Python** utilizando el framework **Flask** para el backend, **HTML y CSS** para el frontend estático, y **SQLite** como base de datos. Además, el proyecto está preparado para ejecutarse dentro de un contenedor de **Docker**.

## Características

- Añadir, eliminar y listar tareas.
- Interfaz sencilla con un frontend estático (HTML y CSS).
- Base de datos SQLite para almacenar las tareas.
- Contenerización con Docker para portabilidad y despliegue fácil.

## Requisitos previos

Antes de ejecutar este proyecto, asegúrate de tener instalados los siguientes componentes:

- Python 3.9 o superior
- Flask
- Flask-SQLAlchemy
- Docker (opcional para contenerización)



# Estructura del proyecto 
<img width="565" alt="image" src="https://github.com/user-attachments/assets/8be79efe-c12c-4939-8f8c-8875ddc614c1">

# Contenerización con Docker
Para ejecutar la aplicación utilizando contenedores de Docker, seguir estos pasos:
1. **Construir la imagen de Docker**:

   ```bash
   docker build -t todo-app .
2.  **Ejecutar el contenedor**:
Una vez que la imagen esté construida, ejecuta el contenedor en modo detached (-d) y expón el puerto 5000:
  ```bash
  docker run -d -p 5000:5000 todo-app
```

# Uso
- Añadir tarea: Escribe el nombre de una nueva tarea en el formulario y haz clic en "Añadir".
- Eliminar tarea: Haz clic en "Borrar" junto a la tarea que deseas eliminar.

## Autores
- Esteban Samayoa
- Nickolas Nolte


# Cloud Inhouse & Infrastructure
# To-Do List App

Este proyecto es una aplicación de **To-Do List** desarrollada en **Python** utilizando el framework **Flask** para el backend, **HTML y CSS** para el frontend estático, y **SQLite** como base de datos. Además, el proyecto está preparado para ejecutarse dentro de un contenedor de **Docker**.

## Tech Stack
- **Base de Datos:** Dynamo DB
- **Backend:** Lambda, Python
- **FrontEnd:** HTML, CSS

## Características

- Añadir, eliminar y listar tareas.
- Interfaz sencilla con un frontend estático (HTML y CSS).


## Requisitos previos

Antes de ejecutar este proyecto, asegúrate de tener instalados los siguientes componentes:

- Python 3.9 o superior
- Flask
- Flask-SQLAlchemy
- Docker (opcional para contenerización)


## Pasos para construir la solución en AWS
- Crear una cuenta en AWS
### Base de Datos
- Acceder al servicio de Dynamo DB
 <img width="905" alt="image" src="https://github.com/user-attachments/assets/519086f6-4a4c-48df-b3d9-d2974cd5cc00">

- Ir a la sección de "Tablas" en el menú de la izquierda
- Crear nueva tabla
- Ponerle un nombre a la tabla y un partition key (ejemplo: "task_id)
 <img width="809" alt="image" src="https://github.com/user-attachments/assets/03b7471c-5989-42a6-9e80-c3b3bf5b8cf9">

- Dejar la opción de "Default Settings"

### Función Lambda
- Acceder al servicio de Lambda
 <img width="905" alt="image" src="https://github.com/user-attachments/assets/288d40fa-d1d6-4b6f-a20a-279a144ced25">
- Ir a la sección de "Funciones" en el menú de la izquierda.
- Crear una nueva función
- Ponerle un nombre a la función

### Bucket S3
- Acceder al servicio de S3
 <img width="905" alt="image" src="https://github.com/user-attachments/assets/f3e15276-e833-4e24-b3e5-96f0a358f657">
 
- Ir a la sección de "Buckets" en el meneu de la izquierda
- Crear un nuevo Bucket
- Ponerle un nombre al bucket
- <img width="808" alt="image" src="https://github.com/user-attachments/assets/975bcfdb-753c-4293-bbcf-86a773190c82">
- Deshabilitar la opción de "Block all public access"
 <img width="799" alt="image" src="https://github.com/user-attachments/assets/76977b0c-0e48-4af5-9e37-13ada9a2429f">
 
 <img width="687" alt="image" src="https://github.com/user-attachments/assets/dca189ec-d05d-43bc-9f51-a1a85ccbba6a">
 
- Después de haber creado el Bucket, hay que acceder al mismo.
- Luego, en el apartado de "Objects" se debe cargar el archivo de FrontEnd de la aplicación de ToDo List.
- Seleccionar la opción de "Properties"
 <img width="586" alt="image" src="https://github.com/user-attachments/assets/844bd1a6-ca76-4679-84e0-abc4b62a6faf">
 
- Dirigirse hasta abajo, a la opción de "Static Web Hosting"
 <img width="360" alt="image" src="https://github.com/user-attachments/assets/812d95ae-6d85-4f45-bd4f-9c09913e4c9e">
 
- Presionar el botón de "editar", elegir la opción de "enable" y guardar los cambios.
 <img width="681" alt="image" src="https://github.com/user-attachments/assets/49d37a6c-0947-4ab5-9f59-24f2e196bf94">
 

### Kubernetes

# Uso
- Añadir tarea: Escribe el nombre de una nueva tarea en el formulario y haz clic en "Añadir".
- Eliminar tarea: Haz clic en "Borrar" junto a la tarea que deseas eliminar.

## Autores
- Esteban Samayoa
- Nickolas Nolte


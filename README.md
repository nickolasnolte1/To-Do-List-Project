# Cloud Inhouse & Infrastructure
## To-Do List App

Este proyecto es una aplicación de **To-Do List** desarrollada en **Python** utilizando el framework **Flask** para el backend, **HTML y CSS** para el frontend estático, y **SQLite** como base de datos. Además, el proyecto está preparado para ejecutarse dentro de un contenedor de **Docker**.

---

## 🚀 Tech Stack
- **Base de Datos:** DynamoDB
- **Backend:** AWS Lambda, Python
- **Frontend:** HTML, CSS

---

## 📋 Características
- Añadir, eliminar y listar tareas.
- Interfaz sencilla con un frontend estático (HTML y CSS).

---

## 📦 Requisitos previos

Antes de ejecutar este proyecto, asegúrate de tener instalados los siguientes componentes:

- Python 3.9 o superior
- Flask
- Flask-SQLAlchemy
- Docker (opcional para contenerización)

---

## 🌐 Pasos para construir la solución en AWS

### 1. Crear una cuenta en AWS

### 2. Configuración de la Base de Datos
1. Accede al servicio de DynamoDB.
   ![DynamoDB](https://github.com/user-attachments/assets/519086f6-4a4c-48df-b3d9-d2974cd5cc00)

2. Ir a la sección de "Tablas" en el menú de la izquierda.
3. Crear nueva tabla:
   - Asigna un nombre a la tabla y un **Partition Key** (ejemplo: `task_id`).
   ![Tabla DynamoDB](https://github.com/user-attachments/assets/03b7471c-5989-42a6-9e80-c3b3bf5b8cf9)

4. Dejar la opción de "Default Settings".

### 3. Configuración de la Función Lambda
1. Accede al servicio de Lambda.
   ![Lambda](https://github.com/user-attachments/assets/288d40fa-d1d6-4b6f-a20a-279a144ced25)

2. Ir a la sección de "Funciones" en el menú de la izquierda.
3. Crear una nueva función:
   - Asigna un nombre a la función.
   - Ve a la sección de "Code" y carga o copia el código del backend. **Importante**: presiona "Deploy" cada vez que se haga un cambio.
   ![Code Lambda](https://github.com/user-attachments/assets/0973bbc6-ba7f-4bd2-a41a-0bd76ecd785b)

4. Dirígete a la sección de configuración y selecciona el enlace con el nombre de la función.
   ![Configuración Lambda](https://github.com/user-attachments/assets/62edf846-16bd-44db-b81a-54b17ed5c564)

5. Selecciona la opción de "CORS" en el menú de la izquierda.
   - Coloca un asterisco (*) en cada uno de los campos y guarda los cambios.
   ![CORS Lambda](https://github.com/user-attachments/assets/81be510e-a0c1-4b01-9ab4-0a3d82c146dc)

### 4. Configuración del Bucket S3
1. Accede al servicio de S3.
   ![S3](https://github.com/user-attachments/assets/f3e15276-e833-4e24-b3e5-96f0a358f657)

2. Ir a la sección de "Buckets" en el menú de la izquierda.
3. Crear un nuevo bucket:
   - Asigna un nombre al bucket.
   ![Crear Bucket](https://github.com/user-attachments/assets/975bcfdb-753c-4293-bbcf-86a773190c82)

4. Deshabilita la opción de "Block all public access".
   ![Deshabilitar acceso público](https://github.com/user-attachments/assets/76977b0c-0e48-4af5-9e37-13ada9a2429f)

5. Accede al bucket creado y carga el archivo de frontend de la aplicación de To-Do List en la sección de "Objects".
6. Selecciona la opción de "Properties".
   ![Properties S3](https://github.com/user-attachments/assets/844bd1a6-ca76-4679-84e0-abc4b62a6faf)

7. Dirígete a la sección de "Static Web Hosting" y habilita la opción.
   ![Static Web Hosting](https://github.com/user-attachments/assets/812d95ae-6d85-4f45-bd4f-9c09913e4c9e)
   ![Guardar cambios](https://github.com/user-attachments/assets/49d37a6c-0947-4ab5-9f59-24f2e196bf94)

### 5. Kubernetes (Pendiente)

---

## 📝 Uso
- **Añadir tarea:** Escribe el nombre de una nueva tarea en el formulario y haz clic en "Añadir".
- **Eliminar tarea:** Haz clic en "Borrar" junto a la tarea que deseas eliminar.

---

## 👥 Autores
- **Esteban Samayoa**
- **Nickolas Nolte**

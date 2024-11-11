# Cloud Inhouse & Infrastructure
## To-Do List App

---

## 📚 Tabla de Contenidos
- [Descripción del Proyecto](#💡-descripción-del-proyecto)
- [Tech Stack](#🚀-tech-stack)
- [Características](#📋-características)
- [Requisitos Previos](#📦-requisitos-previos)
- [Pasos para Construir la Solución en AWS](#🌐-pasos-para-construir-la-solución-en-aws)
- [Uso](#📝-uso)
- [Deployment](#🚀-deployment)
- [Autores](#👥-autores)
- [Licencia](#📄-licencia)

---

## 💡 Descripción del Proyecto
La aplicación **To-Do List** permite a los usuarios organizar sus tareas diarias de manera sencilla y eficiente. El objetivo es proporcionar una interfaz simple para que cualquier persona pueda gestionar sus pendientes, mientras que en el backend se utilizan servicios de AWS para asegurar escalabilidad y disponibilidad en la nube.

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

### 2. Crear un usuario en IAM

1. **Accede al servicio de IAM** en la consola de AWS.
   - ![Acceder a IAM](https://github.com/user-attachments/assets/3fe773ed-cc03-4b59-9f17-e4fb93398ca3)

2. **Crea un nuevo rol** en IAM.
   - <img width="1050" alt="image" src="https://github.com/user-attachments/assets/57b2ae28-49cb-4d52-9d27-44ede59eb689">

4. En "trusted entity type" seleccionar AWS Service.
5. En "Use Case" seleccionar DynamoDB y "Amazon Dynamo DB Accelerator (DAX) - Dynamo DB Access.

6. **Asigna los siguientes permisos** al usuario para que tenga acceso a los servicios necesarios:
   - `AmazonDynamoDBFullAccess`
  
7. **Asigna un nombre** descriptivo al rol para identificarlo fácilmente.

8. Finaliza la creación del rol siguiendo los pasos restantes en la consola de AWS.



### 3. Configuración de la Base de Datos (DynamoDB)
1. Accede al servicio de DynamoDB en tu consola de AWS.
 - ![DynamoDB](https://github.com/user-attachments/assets/519086f6-4a4c-48df-b3d9-d2974cd5cc00)
2. En la sección de "Tablas" en el menú de la izquierda, selecciona **Crear nueva tabla**.
3. Asigna un nombre a la tabla y un **Partition Key** (`task_id`).
4. Deja la opción de "Default Settings" activada y crea la tabla.

### 4. Configuración de la Función Lambda
1. Accede al servicio de Lambda en tu consola de AWS.
   - ![Lambda](https://github.com/user-attachments/assets/288d40fa-d1d6-4b6f-a20a-279a144ced25)
2. En la sección de "Funciones", selecciona **Crear una nueva función**.
   - Asigna un nombre a la función.
   - Selecciona la opción de "Use a Blueprint"
   - Seleccionar la opción que dice "Create a microservice that interacts with a DDBB table" con Python 3.10
   - <img width="711" alt="image" src="https://github.com/user-attachments/assets/ab9436ad-a323-4b30-a9b4-ff1bbad98e20">

3. En la sección de "Code", carga o copia el código del backend. **Recuerda** presionar "Deploy" cada vez que hagas un cambio.
   - ![Code Lambda](https://github.com/user-attachments/assets/0973bbc6-ba7f-4bd2-a41a-0bd76ecd785b)
4. Ve a la sección de configuración y selecciona el enlace con el nombre de la función.
   - ![Configuración Lambda](https://github.com/user-attachments/assets/62edf846-16bd-44db-b81a-54b17ed5c564)
5. En la opción "CORS" en el menú de la izquierda, coloca un asterisco (*) en cada campo y guarda los cambios.
   - ![CORS Lambda](https://github.com/user-attachments/assets/81be510e-a0c1-4b01-9ab4-0a3d82c146dc)

### 5. Configuración del Bucket S3
1. Accede al servicio de S3 en tu consola de AWS.
   - ![S3](https://github.com/user-attachments/assets/f3e15276-e833-4e24-b3e5-96f0a358f657)
2. En la sección de "Buckets", selecciona **Crear un nuevo bucket**.
   - Asigna un nombre al bucket.
   - ![Crear Bucket](https://github.com/user-attachments/assets/975bcfdb-753c-4293-bbcf-86a773190c82)
3. Deshabilita la opción de "Block all public access".
   - ![Deshabilitar acceso público](https://github.com/user-attachments/assets/76977b0c-0e48-4af5-9e37-13ada9a2429f)
4. Accede al bucket creado y carga el archivo del frontend de la aplicación en la sección de "Objects".
5. Selecciona la opción de "Properties".
   - ![Properties S3](https://github.com/user-attachments/assets/844bd1a6-ca76-4679-84e0-abc4b62a6faf)
6. En la sección "Static Web Hosting", habilita la opción.
   - ![Static Web Hosting](https://github.com/user-attachments/assets/812d95ae-6d85-4f45-bd4f-9c09913e4c9e)
   - ![Guardar cambios](https://github.com/user-attachments/assets/49d37a6c-0947-4ab5-9f59-24f2e196bf94)


---

## 📝 Uso
- **Añadir tarea:** Escribe el nombre de una nueva tarea en el formulario y haz clic en "Añadir".
- **Eliminar tarea:** Haz clic en "Borrar" junto a la tarea que deseas eliminar.

---

## 👥 Autores
- **Esteban Samayoa**
- **Nickolas Nolte**

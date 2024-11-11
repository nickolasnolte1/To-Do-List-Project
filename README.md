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

### 1. Descargar el archivo de frontend de este repositorio y abrirlo en VSC, más adelante lo usaremos.

### 2. Crear un Rol en IAM

1. **Accede al servicio de IAM** en la consola de AWS.
   - ![Acceder a IAM](https://github.com/user-attachments/assets/3fe773ed-cc03-4b59-9f17-e4fb93398ca3)

2. **Crea un nuevo rol** en IAM seleccionando la opción para roles.
   - ![Crear rol](https://github.com/user-attachments/assets/57b2ae28-49cb-4d52-9d27-44ede59eb689)

3. En la sección **Trusted entity type**, selecciona **AWS Service** como tipo de entidad de confianza.

4. En el campo **Use Case**, elige **Lambda**.
   - <img width="807" alt="image" src="https://github.com/user-attachments/assets/5d3e25e8-9fd8-44d0-9846-db79131a339e">


5. **Asigna los permisos necesarios** al rol para que tenga acceso a los servicios requeridos:
   - `AmazonDynamoDBFullAccess`

6. **Asigna un nombre descriptivo** al rol para identificarlo fácilmente en tu lista de roles.

7. **Finaliza la creación del rol** siguiendo los pasos restantes en la consola de AWS.


### 3. Configuración de la Base de Datos (DynamoDB)

1. **Accede al servicio de DynamoDB** en la consola de AWS.
   - ![DynamoDB](https://github.com/user-attachments/assets/519086f6-4a4c-48df-b3d9-d2974cd5cc00)

2. En el menú de la izquierda, ve a la sección **Tablas** y selecciona **Crear nueva tabla**.

3. **Asigna un nombre** a la tabla y configura el **Partition Key** con el nombre `task_id`.
   - Este campo `task_id` será el identificador único de cada tarea en la tabla.

4. **Mantén activada la opción "Default Settings"** para que AWS configure automáticamente los parámetros predeterminados de capacidad y seguridad.

5. Haz clic en **Crear tabla** para finalizar la configuración.


### 4. Configuración de la Función Lambda

1. **Accede al servicio de Lambda** en la consola de AWS.
   - ![Lambda](https://github.com/user-attachments/assets/288d40fa-d1d6-4b6f-a20a-279a144ced25)

2. En la sección de **Funciones**, selecciona **Crear una nueva función**.
   - Asigna un **nombre descriptivo** a la función.
   - Selecciona la opción **"Use a Blueprint"**.
   - En los blueprints disponibles, selecciona **"Create a microservice that interacts with a DDBB table"** y elige **Python 3.10** como runtime.
   - ![Blueprint Lambda](https://github.com/user-attachments/assets/ab9436ad-a323-4b30-a9b4-ff1bbad98e20)

3. En la configuración de permisos, selecciona **"Use an existing role"** y elige el rol que creaste anteriormente en IAM para este propósito.

4. En la sección de **API Gateway trigger**:
   - Selecciona **Create New API** y elige **HTTP API** como tipo de API.
   - En **Seguridad**, selecciona **"open"** para habilitar acceso sin autenticación.
   - ![API Gateway Trigger](https://github.com/user-attachments/assets/c9accd23-8ef3-4cfe-9a1c-fca001f82ecf)

5. Haz clic en **Crear función** para finalizar la configuración inicial de la función Lambda.

6. En la sección de **Code**, carga o copia el código del backend (archivo `app.py`). **Recuerda** presionar **Deploy** cada vez que realices cambios en el código para que se apliquen.
   - ![Code Lambda](https://github.com/user-attachments/assets/0973bbc6-ba7f-4bd2-a41a-0bd76ecd785b)

7. Ve a la sección de **Configuration** y selecciona el enlace con el nombre de la función para abrir una nueva pestaña de configuración avanzada.
   - ![Configuración Lambda](https://github.com/user-attachments/assets/62edf846-16bd-44db-b81a-54b17ed5c564)

8. En el menú de la izquierda, selecciona **CORS** (Cross-Origin Resource Sharing):
   - Haz clic en **Configure** y coloca un asterisco (*) en cada campo para permitir acceso desde cualquier origen.
   - Guarda los cambios.
   - ![Configuración CORS](https://github.com/user-attachments/assets/42c94eeb-6765-4812-bacf-68a51684f3fa)

9. Puedes cerrar la pestaña de configuración una vez que hayas guardado todos los cambios.



### 5. Configuración del Bucket S3

1. **Accede al servicio de S3** en tu consola de AWS.
   - ![S3](https://github.com/user-attachments/assets/f3e15276-e833-4e24-b3e5-96f0a358f657)

2. En la sección **Buckets**, selecciona **Crear un nuevo bucket**.
   - Asigna un **nombre único** al bucket para identificarlo en tu proyecto.
   - ![Crear Bucket](https://github.com/user-attachments/assets/975bcfdb-753c-4293-bbcf-86a773190c82)

3. **Deshabilita la opción "Block all public access"** para permitir el acceso público al contenido del bucket.
   - Esto es necesario para que el frontend de la aplicación sea accesible desde internet.
   - ![Deshabilitar acceso público](https://github.com/user-attachments/assets/76977b0c-0e48-4af5-9e37-13ada9a2429f)


4. En el menú del bucket, selecciona **Properties**.
   - ![Properties S3](https://github.com/user-attachments/assets/844bd1a6-ca76-4679-84e0-abc4b62a6faf)

5. En la sección **Static Web Hosting**, habilita la opción para que el bucket pueda servir el contenido del frontend como un sitio web estático.
   - Haz clic en **Editar**, elige la opción **Enable**, y guarda los cambios.
   - ![Static Web Hosting](https://github.com/user-attachments/assets/812d95ae-6d85-4f45-bd4f-9c09913e4c9e)
   - ![Guardar cambios](https://github.com/user-attachments/assets/49d37a6c-0947-4ab5-9f59-24f2e196bf94)

Con estos pasos, tu bucket S3 estará configurado para servir el frontend de la aplicación como un sitio web estático.

### 6. Deploy

1. **Accede al servicio de Lambda** en la consola de AWS para obtener el enlace del API Endpoint.

2. **Copia el enlace del API Endpoint** generado para tu función Lambda.
   - Este enlace permite que el frontend se comunique con el backend.
   - ![API Endpoint](https://github.com/user-attachments/assets/0de64cd6-15be-4e3f-9bee-97711c15ad68)

3. **Actualiza el archivo `index.html` del frontend**:
   - Abre el archivo `index.html`.
   - En la línea 93, reemplaza la URL existente con el **API Endpoint** copiado.
   - ![Actualizar URL](https://github.com/user-attachments/assets/7758e581-0b11-45c4-ae88-6c3c738823ca)
   - Guarda el archivo después de realizar el cambio.

4. **Sube el archivo HTML actualizado** al bucket S3:
   - Accede a tu bucket S3 configurado para el frontend y carga el archivo `index.html` modificado. Esto permite que el frontend haga peticiones al backend a través del API Endpoint.

5. **Inicia Google Chrome con CORS deshabilitado** (para pruebas locales):
   - Abre la terminal en tu computadora y ejecuta el siguiente comando según tu sistema operativo:
   - **MacOS**:
     ```bash
     open -na "Google Chrome" --args --disable-web-security --user-data-dir="/tmp/chrome_dev"
     ```
   - **Windows**:
     ```bash
     "C:\Program Files\Google\Chrome\Application\chrome.exe" --disable-web-security --user-data-dir="C:/chrome_dev"
     ```
   - Este comando abre Chrome con CORS deshabilitado, permitiendo que el frontend se comunique con el backend sin restricciones de seguridad de origen.

6. **Accede a la aplicación**:
   - Copia el enlace de **Object URL** de tu archivo HTML en S3 y pégalo en Google Chrome (con CORS deshabilitado).
   - ![Object URL](https://github.com/user-attachments/assets/0de75fb7-9a0e-4178-ace3-6a447b51cb1b)



---

## 📝 Uso
- **Añadir tarea:** Escribe el nombre de una nueva tarea en el formulario y haz clic en "Añadir".
- **Eliminar tarea:** Haz clic en "Borrar" junto a la tarea que deseas eliminar.

---

## 👥 Autores
- **Esteban Samayoa**
- **Nickolas Nolte**

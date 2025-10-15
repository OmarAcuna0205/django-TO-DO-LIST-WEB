# 🐳 Entorno Fullstack con Docker  
## Django + React + PostgreSQL + pgAdmin

Este entorno te permite desarrollar una aplicación web completa sin instalar Python, Node.js ni PostgreSQL. Todo corre dentro de contenedores Docker.

---

## 🧱 Contenidos del proyecto

| Servicio       | Tecnología                       | Función                              |
|----------------|----------------------------------|--------------------------------------|
| `postgres_db`  | PostgreSQL 16                    | Base de datos relacional             |
| `pgadmin`      | pgAdmin 4                        | Interfaz web para manejar PostgreSQL |
| `django_app`   | Python 3.12 + Django + DRF       | Backend con API REST                 |
| `react_app`    | Node 20 + Vite + React           | Frontend con recarga automática      |

---

## ✅ Requisitos

- Tener **Docker** y **Docker Compose** instalados.
- Haber recibido esta carpeta `proyecto_fullstack/` completa por USB, ZIP, etc.

---

## 🚀 Pasos para levantar el entorno por primera vez

### 📂 1. Abrir terminal en la carpeta del proyecto

```bash
cd ruta/del/proyecto_fullstack
📁 2. Crear carpetas necesarias para los datos
Estos directorios se usarán para guardar datos de la base y pgAdmin (persistencia):

bash
Copy code
mkdir -p data/postgres data/pgadmin
En Linux/WSL da permisos:

bash
Copy code
chmod -R 777 data
⚙️ 3. Construir los contenedores
bash
Copy code
docker-compose build
Esto hará lo siguiente automáticamente:

Instalará Django, DRF y React dentro de los contenedores.

Creará el proyecto Django si no existe.

Creará el proyecto React si no existe.

▶️ 4. Iniciar todos los servicios
bash
Copy code
docker-compose up
Espera a que todos los servicios se inicien.
La primera vez puede tardar de 1 a 5 minutos.

🌐 Accesos desde el navegador
Servicio	URL
Django	http://localhost:8000
React (Vite)	http://localhost:5173
pgAdmin	http://localhost:5050

🔐 Datos de acceso pgAdmin
Usuario: admin@admin.com

Contraseña: admin

Para conectar pgAdmin a la base de datos:
Campo	Valor
Host	postgres_db
Puerto	5432
Usuario	myuser
Contraseña	123
Base de datos	mydb

🛠️ Comandos útiles para trabajar con los contenedores
Ver logs en vivo
bash
Copy code
docker-compose up
Apagar todos los contenedores
Presiona CTRL + C y luego:

bash
Copy code
docker-compose down
Ver contenedores corriendo
bash
Copy code
docker ps
Entrar al contenedor de Django
bash
Copy code
docker-compose exec django_app sh
Crear superusuario de Django
bash
Copy code
docker-compose exec django_app python manage.py createsuperuser
📂 Estructura esperada
lua
Copy code
proyecto_fullstack/
├── backend/
│   ├── Dockerfile
│   ├── create-django.sh
│   └── requirements.txt
├── frontend/
│   ├── Dockerfile
│   └── create-react.sh
├── data/
│   ├── postgres/
│   └── pgadmin/
├── docker-compose.yml
└── README.md
🧠 ¿Qué hace este entorno?
Si no existe un proyecto Django, se crea automáticamente.

Si no existe un proyecto React, se crea automáticamente.

Puedes editar tu backend en backend/ y tu frontend en frontend/.

Los cambios se reflejan automáticamente gracias al volumen compartido.

Este entorno está listo para usarse como base de desarrollo web fullstack sin dependencias externas.
Ideal para clases, talleres o prácticas educativas con Django y React.











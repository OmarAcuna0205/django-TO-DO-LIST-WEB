# backend/Dockerfile

# Imagen base de Python
FROM python:3.12-slim

# Crear directorio de trabajo
WORKDIR /app

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    libpq-dev gcc netcat-traditional && \
    rm -rf /var/lib/apt/lists/*

# Copiar archivo de requerimientos e instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el script de creación automática de Django
COPY create-django.sh /create-django.sh
RUN chmod +x /create-django.sh

# Copiar el resto del backend (aunque esté vacío al principio)
COPY . .

# Ejecutar el script
CMD ["/create-django.sh"]

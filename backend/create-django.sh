#!/bin/sh

# Esperar a que la base de datos esté lista
echo "Esperando a que postgres esté disponible..."
while ! nc -z postgres_db 5432; do
  sleep 2
done
echo "Base de datos lista."

# Si no existe el archivo manage.py, crear el proyecto
if [ ! -f manage.py ]; then
  echo "Proyecto Django no encontrado. Creando uno..."
  django-admin startproject backend .
fi

# Migraciones iniciales
echo "Aplicando migraciones..."
python manage.py migrate

# Ejecutar el servidor
echo "Levantando servidor Django en http://localhost:8000"
python manage.py runserver 0.0.0.0:8000

# backend/tasks/admin.py

from django.contrib import admin
from .models import Task, Category # Importamos ambos modelos

admin.site.register(Task)
admin.site.register(Category)

# backend/tasks/models.py

from django.db import models
from django.utils import timezone

# --- 1. NUEVO MODELO PARA LAS CATEGORÍAS ---
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Baja'),
        (2, 'Media'),
        (3, 'Alta'),
    ]

    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    completed = models.BooleanField(default=False, verbose_name="Completada")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Creación")
    
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES, 
        default=2,
        verbose_name="Prioridad"
    )

    due_date = models.DateField(null=True, blank=True, verbose_name="Fecha Límite")

    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name="Materia"
    )


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

    @property
    def is_overdue(self):
        if self.due_date and timezone.now().date() > self.due_date:
            return not self.completed
        return False

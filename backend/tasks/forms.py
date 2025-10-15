# backend/tasks/forms.py

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        
        # AÑADIMOS 'category' A LA LISTA
        fields = ['title', 'description', 'priority', 'due_date', 'category']

        widgets = {
            'due_date': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            ),
            # No necesitamos widget para 'category', Django usará un dropdown por defecto.
        }

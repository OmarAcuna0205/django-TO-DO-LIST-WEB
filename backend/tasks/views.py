from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Category
from .forms import TaskForm # Asegúrate de que TaskForm esté importado
from django.contrib import messages # Importar el módulo messages

# Create your views here.
# Vista para mostrar la lista de tareas
def task_list(request):
    # Obtiene el modo de vista. El valor por defecto es 'pending'.
    view_mode = request.GET.get('view_mode', 'pending')

    # === CORRECCIÓN #1 ===
    # En lugar de filtrar por usuario, obtenemos TODAS las tareas.
    tasks = Task.objects.all()

    # Aplica el filtro de estado según el modo de vista.
    if view_mode == 'completed':
        tasks = tasks.filter(completed=True)
    else: # Por defecto, y si es 'pending', muestra solo las no completadas.
        tasks = tasks.filter(completed=False)

    # El resto de filtros (búsqueda, categoría, orden) se aplican sobre el resultado anterior.
    search_query = request.GET.get('search-area', '')
    if search_query:
        tasks = tasks.filter(title__icontains=search_query)

    category_query = request.GET.get('category', '')
    if category_query:
        tasks = tasks.filter(category__id=category_query)

    orderby_query = request.GET.get('orderby', 'created_at')
    tasks = tasks.order_by(orderby_query)

    # === CORRECCIÓN #2 ===
    # Los contadores también se calculan sobre el total de tareas, sin filtrar por usuario.
    all_tasks_for_counts = Task.objects.all()
    total_tasks = all_tasks_for_counts.count()
    pending_tasks = all_tasks_for_counts.filter(completed=False).count()
    completed_tasks = all_tasks_for_counts.filter(completed=True).count()
    
    # === CORRECCIÓN #3 ===
    # Obtenemos todas las categorías sin filtrar por usuario.
    all_categories = Category.objects.all()

    context = {
        'tasks': tasks,
        'search_query': search_query,
        'all_categories': all_categories,
        'total_tasks': total_tasks,
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks,
        'current_view_mode': view_mode,
    }
    return render(request, 'tasks/task_list.html', context)


# Vista para ver el detalle de una tarea
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})


# Vista para crear una nueva tarea
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡La tarea ha sido creada exitosamente!') # Mensaje de éxito
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


# Vista para editar una tarea existente
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, '¡La tarea ha sido actualizada exitosamente!') # Mensaje de éxito
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})


# Vista para eliminar una tarea
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, '¡La tarea ha sido eliminada exitosamente!') # Mensaje de éxito
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


# Vista para marcar una tarea como completada o pendiente
def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    if task.completed:
        messages.info(request, f'¡La tarea "{task.title}" ha sido marcada como completada!') # Mensaje informativo
    else:
        messages.info(request, f'¡La tarea "{task.title}" ha sido marcada como pendiente!') # Mensaje informativo
    return redirect('task_list')


from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from toDo_task.form import TodoForm
from toDo_task.models import TaskModel

# Create your views here.
class home(TemplateView):
  template_name = 'home.html'

## submit Your ToDoTask
def submit_task(request):
  if request.method == 'POST':
    form = TodoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('show_taskpage')
  else:
    form = TodoForm()
  return render(request, 'submit_task.html', {'form':form})

## Show ToDoTask
def show_task(request):
  todo = TaskModel.objects.all()
  
  return render(request, 'show_tasks.html', {'todo':todo})

## Delete ToDoTask
def Delete_task(request,id):
  task = TaskModel.objects.get(pk=id).delete()
  return redirect('show_taskpage')

## Edit ToDoTask
def edit_task(request,id):
  Task = TaskModel.objects.get(pk=id)
  form = TodoForm(instance=Task)
  if request.method == 'POST':
    form = TodoForm(request.POST, instance=Task)
    if form.is_valid():
      form.save()
      return redirect('show_taskpage')
  return render(request, 'submit_task.html', {'form':form})
  

## Complete ToDoTask
def complete_task(requset, id):
  task = TaskModel.objects.get(pk = id)
  if task.is_completed == False:
    task.is_completed = True
    task.save()
    
  return redirect('show_complete_taskpage')
  
## show complete ToDoTask
def Show_complete_task(request):
  task = TaskModel.objects.all()
  return render(request, 'complete_task.html', {'task':task})


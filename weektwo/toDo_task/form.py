from django import forms
from toDo_task.models import TaskModel

class TodoForm(forms.ModelForm):
  class Meta:
    model = TaskModel
    fields = ['taskTitle', 'taskDescription']
    
  
  
    


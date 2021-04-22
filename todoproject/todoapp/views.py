
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from todoapp.forms import Todoform
from todoapp.models import Task


def task_view(request):
    if request.method=="POST":
        name=request.POST.get('name')
        priority= request.POST.get('priority')
        date=request.POST.get('date')
        obj=Task(name=name,priority=priority,date=date)
        obj.save()

    obj1=Task.objects.all()
    return render(request, 'taskview.html', {'obj11': obj1})


# def task(request):
#
#     return render(request, 'task.html')
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{'taask':task})

def update(request,id):
    task=Task.objects.get(id=id)
    form=Todoform(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'form':form})


class TaskList(ListView):
    model = Task
    template_name ='taskview.html'
    context_object_name = 'obj11'

class TaskD(DetailView):
    model =Task
    template_name ='detail.html'
    context_object_name = 'i'

class TaskU(UpdateView):
    model =Task
    template_name ='update.html'
    context_object_name = 'task'
    fields=('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class Taskd(DeleteView):
    model= Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvtask')
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from tasks.forms import TaskForm
from tasks.models import Task


# Create your views here.
@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()

    context = {"form": form}
    return render(request, "tasks/create.html", context)


class show_my_tasks(ListView):
    model = Task
    template_name = "tasks/mine.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)

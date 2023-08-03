from django.shortcuts import render
from projects.models import Project


# Create your views here.
def list_projects(request):
    project = Project.objects.all()
    context = {"project_obj": project}
    return render(request, "projects/list.html", context)

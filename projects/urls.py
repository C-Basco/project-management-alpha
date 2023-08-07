from django.urls import path, include
from projects.views import list_projects


urlpatterns = [
    path("", list_projects, name="list_projects"),
]

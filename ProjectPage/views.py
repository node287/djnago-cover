from django.shortcuts import render, get_object_or_404
from .models import ProjectModels

def DispalyAllProjects(request):
    Projects = ProjectModels.objects
    return render(request, 'ProjectPage/displayallprojects.html', {'projects':Projects})

def DisplayOneProject(request, project_id):
    Project = get_object_or_404(ProjectModels, pk=project_id)
    return render(request, 'ProjectPage/displayOneProject.html', {'project':Project})
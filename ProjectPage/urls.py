from django.urls import path
import ProjectPage.views

urlpatterns = [
    path('', ProjectPage.views.DispalyAllProjects, name='projects'),
    path('<int:project_id>', ProjectPage.views.DisplayOneProject, name='displayOneProject')
]

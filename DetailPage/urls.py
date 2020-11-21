from django.urls import path
import DetailPage.views

urlpatterns = [
    path('', DetailPage.views.welcomeScreen, name='home'),
]
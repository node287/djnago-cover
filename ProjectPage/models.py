from django.db import models


class ProjectModels(models.Model):
    image = models.ImageField(upload_to='projectImages/')
    title = models.CharField(max_length=100)
    description =  models.CharField(max_length=800)
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:120]+"..."
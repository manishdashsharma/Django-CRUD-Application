from django.db import models
#from django.core.validators import MinLengthValidator

# Create your models here.

class StudyMaterial(models.Model):
    # date = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    subjectName = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    video = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
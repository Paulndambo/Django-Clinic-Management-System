from django.db import models

# Create your models here.
class Birthday(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.name
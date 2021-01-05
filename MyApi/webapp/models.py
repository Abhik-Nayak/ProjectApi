from django.db import models

# Create your models here.
class employees(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    work_as=models.CharField(max_length=20)
    Experience_years=models.IntegerField()

    def __str__(self):
        return self.firstname
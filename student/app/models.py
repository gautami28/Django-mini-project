from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Studdata(models.Model):
    #user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    clas = models.CharField(max_length=200)
    rollno = models.IntegerField()
    FEcgpa = models.FloatField()
    Hobbies = models.CharField(max_length=200)
    Reviews = models.CharField(max_length=200)

    BRANCH_CHOICES = (
    ('AI&DS','AI&DS'),
    ('COMPUTER','COMPUTER'),
    ('IT','IT'),
    ('CIVIL','CIVIL'),
    ('MECHANICAL','MECHANICAL'),
    ('ROBOTICS & AUTOMATION','ROBOTICS & AUTOMATION'),
    )


    def __str__(self):
        return str(self.id)

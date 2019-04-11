from django.db import models
from apps.users.models import User


# Create your models here.
categor = (('desarrollo','desarrollo'),('comunidad','comunidad'))
stat = (('ejecucion','ejecucion'),('terminacion','terminacion'))
class Task(models.Model):
    task = models.CharField(max_length=90)
    category = models.CharField(choices=categor, max_length=30)
    date_init = models.DateField()
    date_finish = models.DateField()
    state = models.CharField(choices=stat, max_length=30)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)


from django.db import models
import time
# Create your models here.
class Priloshenie((models.Model)):
    Name=models.CharField()
    Text = models.CharField()
    Pub_Date=models.TimeField()
    Reiting=[]
class ButtonFind((models.Model)):
    NameB=models.CharField()
    Bull=models.BooleanField()

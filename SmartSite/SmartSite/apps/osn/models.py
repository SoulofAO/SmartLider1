from django.db import models
import time
# Create your models here.
class Priloshenie((models.Model)):
    Name=models.CharField("название", max_length=200)
    Text = models.TextField("Текст")
    Pub_Date=models.DateTimeField("Дата создания")
   # Reiting=models.IntegerField


    #def getInfo(self):
        #return self.Reiting



    def __str__(self):
        return self.Name
    class Meta:
        verbose_name="Приложение"

class ButtonFind((models.Model)):
    NameB=models.CharField("Название Кнопки",max_length=50)
    Bull=models.BooleanField("Зажато/НеЗажато")

    class Meta:
     verbose_name = "Кнопка для поиска"


class Comment((models.Model)):
    priloshenie=models.ForeignKey(Priloshenie,on_delete=models.CASCADE)
    Name=models.CharField("название", max_length=50)
    Text = models.TextField("Текст")
    Pub_Date=models.DateTimeField("Дата создания")
    #Reiting=models.IntegerField

    class Meta:
     verbose_name = "Комментарий"

class User((models.Model)):
    name=models.CharField("name", max_length=200)
    email=models.CharField("email", max_length=200)
    parrol=models.CharField("parrol", max_length=200)

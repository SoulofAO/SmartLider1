from django.db import models
import time
# Create your models here.
class Priloshenie((models.Model)):
    Name=models.CharField("название", max_length=200)
    Text = models.TextField("Текст")
    Pub_Date=models.DateTimeField("Дата создания")
    Reiting=[]

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

    class Meta:
     verbose_name = "Комментарий"

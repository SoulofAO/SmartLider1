from django.db import models

# Create your models here.
class Aplication((models.Model)):
    Name = models.CharField("название", max_length=200)
    Text = models.TextField("Текст")
    Pub_Date = models.DateTimeField("Дата создания")


    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Приложение"
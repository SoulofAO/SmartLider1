# Generated by Django 3.1.3 on 2020-11-28 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osn', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buttonfind',
            options={'verbose_name': 'Кнопка для поиска'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий'},
        ),
        migrations.AlterModelOptions(
            name='priloshenie',
            options={'verbose_name': 'Приложение'},
        ),
    ]
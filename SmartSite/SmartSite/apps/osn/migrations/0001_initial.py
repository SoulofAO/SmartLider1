# Generated by Django 3.1.3 on 2020-11-27 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ButtonFind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameB', models.CharField(max_length=50, verbose_name='Название Кнопки')),
                ('Bull', models.BooleanField(verbose_name='Зажато/НеЗажато')),
            ],
        ),
        migrations.CreateModel(
            name='Priloshenie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, verbose_name='название')),
                ('Text', models.TextField(verbose_name='Текст')),
                ('Pub_Date', models.DateTimeField(verbose_name='Дата создания')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='название')),
                ('Text', models.TextField(verbose_name='Текст')),
                ('Pub_Date', models.DateTimeField(verbose_name='Дата создания')),
                ('priloshenie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='osn.priloshenie')),
            ],
        ),
    ]
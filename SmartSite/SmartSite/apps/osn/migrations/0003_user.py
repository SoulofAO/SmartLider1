# Generated by Django 3.1.3 on 2020-11-28 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osn', '0002_auto_20201128_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('email', models.CharField(max_length=200, verbose_name='email')),
                ('parrol', models.CharField(max_length=200, verbose_name='parrol')),
            ],
        ),
    ]

# Generated by Django 3.2.16 on 2022-10-30 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab1_App', '0005_auto_20221030_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(default='user', max_length=1000),
        ),
    ]
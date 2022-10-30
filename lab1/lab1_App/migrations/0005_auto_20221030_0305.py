# Generated by Django 3.2.16 on 2022-10-30 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab1_App', '0004_auto_20221030_0123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AddField(
            model_name='comments',
            name='match',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lab1_App.matches'),
            preserve_default=False,
        ),
    ]

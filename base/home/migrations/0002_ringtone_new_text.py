# Generated by Django 4.1 on 2022-08-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ringtone',
            name='new_text',
            field=models.TextField(default='NO', max_length=250),
        ),
    ]

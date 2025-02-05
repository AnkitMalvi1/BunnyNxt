# Generated by Django 4.1 on 2022-09-06 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_payment_inr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('1', 'in Review'), ('2', 'Success')], default='in Review', max_length=20),
        ),
        migrations.AlterField(
            model_name='ringtone',
            name='description',
            field=models.TextField(max_length=250),
        ),
    ]

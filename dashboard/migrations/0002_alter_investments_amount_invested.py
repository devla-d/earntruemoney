# Generated by Django 4.0.3 on 2022-05-08 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investments',
            name='amount_invested',
            field=models.IntegerField(default=0),
        ),
    ]
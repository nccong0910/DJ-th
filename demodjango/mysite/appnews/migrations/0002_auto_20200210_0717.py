# Generated by Django 3.0.3 on 2020-02-10 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appnews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

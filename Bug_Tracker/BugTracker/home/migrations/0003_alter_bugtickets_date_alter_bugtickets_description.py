# Generated by Django 4.0 on 2022-01-07 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_bugtickets_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugtickets',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bugtickets',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
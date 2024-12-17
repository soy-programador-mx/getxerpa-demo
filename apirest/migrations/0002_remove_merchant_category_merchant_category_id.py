# Generated by Django 5.0.1 on 2024-12-17 03:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apirest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchant',
            name='category',
        ),
        migrations.AddField(
            model_name='merchant',
            name='category_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.RESTRICT, to='apirest.category'),
        ),
    ]
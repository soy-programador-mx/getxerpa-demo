# Generated by Django 5.0.1 on 2024-12-17 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apirest', '0002_remove_merchant_category_merchant_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[('income', 'Income'), ('expense', 'Expense')], max_length=20),
        ),
    ]
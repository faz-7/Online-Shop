# Generated by Django 4.1.5 on 2023-02-03 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'Paid'), ('U', 'Unpaid')], max_length=1),
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-15 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_remove_ticket_date_of_journey'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='class_type',
            field=models.CharField(max_length=30, null=True),
        ),
    ]

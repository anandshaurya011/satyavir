# Generated by Django 2.2.27 on 2023-07-14 06:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_date_of_birth',
            field=models.DateField(default=datetime.date(2023, 7, 14)),
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-31 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_subject_table_alter_teacher_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='stat_data',
            field=models.DateTimeField(default=True),
        ),
    ]

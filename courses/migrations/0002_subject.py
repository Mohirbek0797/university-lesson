# Generated by Django 4.0.2 on 2022-02-25 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('specialities', models.ManyToManyField(to='courses.Speciality')),
                ('teachers', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courses.teacher')),
            ],
            options={
                'db_table': 'Subject',
            },
        ),
    ]
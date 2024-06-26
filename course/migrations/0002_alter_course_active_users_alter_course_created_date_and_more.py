# Generated by Django 5.0.4 on 2024-04-16 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='active_users',
            field=models.CharField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]

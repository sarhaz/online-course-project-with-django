# Generated by Django 5.0.4 on 2024-04-18 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_alter_course_rating_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='course/course/'),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='image',
            field=models.ImageField(upload_to='course/speciality/'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(upload_to='course/teacher/'),
        ),
    ]
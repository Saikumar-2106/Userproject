# Generated by Django 5.0.6 on 2024-07-07 19:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0005_student_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="Course",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
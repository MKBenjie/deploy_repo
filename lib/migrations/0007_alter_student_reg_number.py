# Generated by Django 4.0.6 on 2022-08-09 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0006_remove_borrowed_user_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='reg_number',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]

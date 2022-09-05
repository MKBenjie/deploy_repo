# Generated by Django 4.0.6 on 2022-08-09 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lib', '0005_book_copies_available_book_total_copies_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowed',
            name='user',
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

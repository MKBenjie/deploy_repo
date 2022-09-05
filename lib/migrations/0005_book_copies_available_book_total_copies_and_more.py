# Generated by Django 4.0.6 on 2022-08-09 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lib', '0004_alter_book_cover_alter_book_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='copies_available',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='total_copies',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='borrowed',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lib.book'),
        ),
        migrations.AddField(
            model_name='borrowed',
            name='issue_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='borrowed',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='borrowed',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lib.student'),
        ),
        migrations.AddField(
            model_name='borrowed',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='student',
            name='college',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='reg_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='total_books_due',
            field=models.IntegerField(default=0),
        ),
    ]

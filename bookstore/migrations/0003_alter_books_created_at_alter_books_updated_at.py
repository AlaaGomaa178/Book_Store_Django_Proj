# Generated by Django 5.0.3 on 2024-03-14 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_books_delete_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
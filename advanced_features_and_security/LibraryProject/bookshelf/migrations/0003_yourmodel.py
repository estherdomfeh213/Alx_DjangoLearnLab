# Generated by Django 5.1.3 on 2024-12-11 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0002_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='YourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'permissions': [('can_view', 'Can view items'), ('can_create', 'Can create items'), ('can_edit', 'Can edit items'), ('can_delete', 'Can delete items')],
            },
        ),
    ]

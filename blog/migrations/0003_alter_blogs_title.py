# Generated by Django 5.0 on 2024-10-17 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogs_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
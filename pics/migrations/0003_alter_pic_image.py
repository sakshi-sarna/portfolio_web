# Generated by Django 5.1.6 on 2025-02-15 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0002_pic_image_pic_month_pic_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='Image',
            field=models.ImageField(upload_to='media/images'),
        ),
    ]

# Generated by Django 5.1.6 on 2025-02-15 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0004_alter_pic_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='Image',
            field=models.ImageField(upload_to=''),
        ),
    ]

# Generated by Django 3.0.6 on 2020-06-03 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0006_auto_20200602_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='instaapp.Image'),
        ),
    ]

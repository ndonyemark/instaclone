# Generated by Django 3.0.6 on 2020-06-02 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0005_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instaapp.Image'),
        ),
    ]

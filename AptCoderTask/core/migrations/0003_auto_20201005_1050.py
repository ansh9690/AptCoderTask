# Generated by Django 3.1.1 on 2020-10-05 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201005_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='description',
            field=models.TextField(),
        ),
    ]
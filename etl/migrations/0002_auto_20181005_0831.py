# Generated by Django 2.1.1 on 2018-10-05 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvdata',
            name='name',
            field=models.CharField(max_length=31),
        ),
    ]

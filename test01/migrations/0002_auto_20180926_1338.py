# Generated by Django 2.0.3 on 2018-09-26 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='difinition',
            name='name',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='difinition',
            name='note',
            field=models.TextField(null=True),
        ),
    ]

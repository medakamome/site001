# Generated by Django 2.0.3 on 2018-09-26 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test01', '0002_auto_20180926_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='difinition',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]

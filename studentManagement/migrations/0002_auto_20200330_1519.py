# Generated by Django 2.0.7 on 2020-03-30 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinformationmodel',
            name='str_addr',
            field=models.CharField(max_length=120, verbose_name='学生地址'),
        ),
    ]

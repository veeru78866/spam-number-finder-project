# Generated by Django 4.1.7 on 2023-03-21 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regApp', '0002_rename_user_name_registerusermodel_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerusermodel',
            name='username',
            field=models.CharField(db_column='username', max_length=20),
        ),
    ]

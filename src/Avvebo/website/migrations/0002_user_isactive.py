# Generated by Django 2.1.5 on 2019-01-17 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
    ]

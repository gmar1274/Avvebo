# Generated by Django 2.1.5 on 2019-01-24 23:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_avveboprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avveboprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

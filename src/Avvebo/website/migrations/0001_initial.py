# Generated by Django 2.1.5 on 2019-01-16 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='TalentContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.CharField(max_length=50)),
                ('date_uploaded', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('reward_points', models.IntegerField(default=0)),
                ('member_since', models.DateField(auto_now_add=True)),
                ('id', models.CharField(max_length=50, unique=True)),
                ('pic_url', models.CharField(max_length=50)),
                ('isTalent', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('member_since', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='talentcontent',
            name='talent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.User'),
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='talent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.User'),
        ),
    ]

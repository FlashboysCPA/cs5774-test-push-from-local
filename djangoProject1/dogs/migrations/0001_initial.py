# Generated by Django 3.2.8 on 2021-10-22 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LostPostStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('url', models.CharField(max_length=200)),
                ('score', models.IntegerField(default=0)),
                ('author', models.CharField(max_length=50)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('contact', models.TextField(blank=True)),
            ],
        ),
    ]

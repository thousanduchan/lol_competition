# Generated by Django 4.2.3 on 2023-09-23 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('members', models.TextField(max_length=1000)),
                ('score', models.IntegerField()),
            ],
        ),
    ]

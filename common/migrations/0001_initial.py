# Generated by Django 4.0.6 on 2022-09-04 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=41)),
                ('school', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.IntegerField()),
                ('birth', models.IntegerField()),
            ],
        ),
    ]

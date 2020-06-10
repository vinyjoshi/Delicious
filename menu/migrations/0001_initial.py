# Generated by Django 3.0.6 on 2020-06-03 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Items', models.TextField()),
                ('price', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('Tag', models.CharField(choices=[('starters', 'STARTERS'), ('salad', 'SALAD'), ('Speciality', 'SPECIALITY')], default=None, max_length=200)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]

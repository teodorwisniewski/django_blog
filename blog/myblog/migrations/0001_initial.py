# Generated by Django 3.2.5 on 2022-02-22 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('author', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('excerpt', models.CharField(max_length=500)),
                ('content', models.TextField()),
            ],
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
    ]

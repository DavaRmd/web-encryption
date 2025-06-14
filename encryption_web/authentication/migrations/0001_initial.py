# Generated by Django 5.2.2 on 2025-06-05 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('no_hp', models.CharField(max_length=13, unique=True)),
                ('nip', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'user_profile',
            },
        ),
    ]

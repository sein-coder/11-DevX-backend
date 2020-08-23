# Generated by Django 3.1 on 2020-08-23 01:38

from django.db import migrations, models
import user.validation


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, validators=[user.validation.Validate_firstname])),
                ('lastname', models.CharField(max_length=100, validators=[user.validation.Validate_lastname])),
                ('email', models.CharField(max_length=100, unique=True, validators=[user.validation.Validate_email])),
                ('password', models.CharField(max_length=100, validators=[user.validation.Validate_password])),
                ('createdtime', models.DateTimeField(auto_now_add=True)),
                ('updatedtime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]

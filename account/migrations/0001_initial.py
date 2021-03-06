# Generated by Django 3.1.1 on 2020-09-22 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20, unique=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='uploads/users/profile_images', verbose_name='profile image')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='is superuser')),
                ('is_staff', models.BooleanField(default=True, verbose_name='is staff')),
                ('is_admin', models.BooleanField(default=True, verbose_name='is admin')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

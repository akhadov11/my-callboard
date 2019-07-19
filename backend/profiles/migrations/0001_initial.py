# Generated by Django 2.2.1 on 2019-06-03 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='profile/')),
                ('second_email', models.EmailField(max_length=254, verbose_name='Additional email')),
                ('phone', models.CharField(max_length=25, verbose_name='Phone number')),
                ('fname', models.CharField(max_length=55, verbose_name='First name')),
                ('lname', models.CharField(max_length=55, verbose_name='Last name')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
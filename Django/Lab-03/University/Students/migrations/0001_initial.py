# Generated by Django 4.2.1 on 2023-05-04 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Birthday', models.DateField()),
            ],
        ),
    ]
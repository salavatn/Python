# Generated by Django 4.2.1 on 2023-05-13 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_db', '0003_alter_vacancies_salary_max_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancies',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_db.currencies'),
        ),
    ]

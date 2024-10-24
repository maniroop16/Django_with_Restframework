# Generated by Django 5.1.2 on 2024-10-24 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=10)),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_designation', models.CharField(max_length=50)),
            ],
        ),
    ]

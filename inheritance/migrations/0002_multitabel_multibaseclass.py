# Generated by Django 5.1.2 on 2024-10-29 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inheritance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Multitabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Multibaseclass',
            fields=[
                ('multitabel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inheritance.multitabel')),
                ('age', models.IntegerField()),
            ],
            bases=('inheritance.multitabel',),
        ),
    ]

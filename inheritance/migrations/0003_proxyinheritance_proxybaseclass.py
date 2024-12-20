# Generated by Django 5.1.2 on 2024-10-29 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inheritance', '0002_multitabel_multibaseclass'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proxyinheritance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProxyBaseclass',
            fields=[
            ],
            options={
                'ordering': ['username'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('inheritance.proxyinheritance',),
        ),
    ]

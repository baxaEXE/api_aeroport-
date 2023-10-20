# Generated by Django 4.2.6 on 2023-10-18 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('characteristics', models.TextField(blank=True, null=True)),
                ('capacity', models.DecimalField(decimal_places=2, default=0, max_digits=2)),
            ],
        ),
    ]

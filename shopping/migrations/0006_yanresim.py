# Generated by Django 4.0.6 on 2022-08-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_rename_buyukcard_buyukcardcocuk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yanresim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yanfoto', models.FileField(blank=True, null=True, upload_to='cards', verbose_name='card resmi')),
            ],
        ),
    ]
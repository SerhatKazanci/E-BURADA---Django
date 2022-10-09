# Generated by Django 4.0.6 on 2022-08-05 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0014_cardkadin'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyukCardKadin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyukfoto', models.FileField(blank=True, null=True, upload_to='cards', verbose_name='card resmi')),
                ('buyukbaslik', models.CharField(max_length=150)),
            ],
        ),
    ]

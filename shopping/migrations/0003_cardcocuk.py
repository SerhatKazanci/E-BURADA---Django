# Generated by Django 4.0.6 on 2022-08-04 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_rename_card_cardindex'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardCocuk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.FileField(blank=True, null=True, upload_to='cards', verbose_name='card resmi')),
                ('baslik', models.CharField(max_length=150)),
                ('metin', models.CharField(max_length=200)),
            ],
        ),
    ]

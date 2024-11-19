# Generated by Django 3.2 on 2024-10-20 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.CharField(default='Kigali', max_length=255),
        ),
        migrations.AddField(
            model_name='patient',
            name='contact_number',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(default='none', max_length=10),
            preserve_default=False,
        ),
    ]

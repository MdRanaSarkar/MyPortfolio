# Generated by Django 3.1 on 2020-08-26 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RanaProtfolio', '0008_auto_20200826_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='workingprotfolio',
            name='location',
            field=models.CharField(default='Dhaka', max_length=200),
            preserve_default=False,
        ),
    ]

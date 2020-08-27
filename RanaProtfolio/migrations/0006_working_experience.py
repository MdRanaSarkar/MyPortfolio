# Generated by Django 3.1 on 2020-08-25 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RanaProtfolio', '0005_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Working_Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w_category', models.CharField(max_length=200)),
                ('W_area', models.CharField(max_length=200)),
                ('w_start_date', models.DateField()),
                ('w_stop_date', models.DateField()),
                ('w_comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

# Generated by Django 2.0 on 2020-05-11 01:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0007_auto_20200510_1627'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='word',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
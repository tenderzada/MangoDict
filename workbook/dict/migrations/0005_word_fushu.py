# Generated by Django 2.0 on 2020-05-10 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0004_auto_20200510_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='fushu',
            field=models.CharField(default='', max_length=100),
        ),
    ]

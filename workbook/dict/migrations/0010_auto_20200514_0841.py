# Generated by Django 2.0 on 2020-05-14 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0009_auto_20200514_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='column',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='column', to='dict.WordColumn'),
        ),
    ]
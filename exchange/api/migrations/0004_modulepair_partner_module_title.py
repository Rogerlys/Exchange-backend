# Generated by Django 3.2.2 on 2021-06-15 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_module_nus_module_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulepair',
            name='partner_module_title',
            field=models.CharField(default='NULL', max_length=50),
            preserve_default=False,
        ),
    ]
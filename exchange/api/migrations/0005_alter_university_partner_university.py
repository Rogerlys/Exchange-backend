# Generated by Django 3.2.3 on 2021-06-10 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_modulepair'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='partner_university',
            field=models.CharField(max_length=100),
        ),
    ]
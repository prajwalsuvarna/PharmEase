# Generated by Django 4.1.2 on 2022-12-03 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_bill_amt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='amt',
            field=models.BigIntegerField(null=True),
        ),
    ]
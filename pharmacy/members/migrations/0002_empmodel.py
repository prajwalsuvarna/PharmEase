# Generated by Django 4.1.2 on 2022-11-15 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpModel',
            fields=[
                ('empname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('e_id', models.IntegerField(primary_key=True, serialize=False)),
                ('mobile', models.IntegerField()),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]

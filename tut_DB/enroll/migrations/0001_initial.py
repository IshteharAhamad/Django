# Generated by Django 3.2.8 on 2021-11-01 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_id', models.IntegerField(primary_key=True, serialize=False)),
                ('roll_No', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('mobile', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 3.2.7 on 2021-10-13 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0010_auto_20211012_0314'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('cid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('className', models.CharField(max_length=36)),
                ('insName', models.CharField(max_length=36)),
                ('days', models.CharField(max_length=20)),
                ('duration', models.SmallIntegerField(default=0)),
                ('max_limit', models.SmallIntegerField(default=30)),
                ('current_enroll', models.SmallIntegerField(default=0)),
                ('wait_list', models.SmallIntegerField(default=0)),
                ('rating', models.FloatField(default=0.0)),
            ],
        ),
        migrations.AddField(
            model_name='stuapplication',
            name='GPA',
            field=models.FloatField(default=0.0),
        ),
    ]

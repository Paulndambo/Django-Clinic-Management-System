# Generated by Django 3.1.7 on 2021-03-17 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20210317_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='quantity',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
# Generated by Django 2.1.5 on 2019-03-03 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20190303_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='hall',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='seat',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='show',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.1.4 on 2021-01-06 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_merge_20210106_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qpapers',
            name='Branch',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='qpapers',
            name='year',
            field=models.IntegerField(default=2021),
        ),
    ]

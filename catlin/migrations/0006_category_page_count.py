# Generated by Django 2.1.7 on 2019-04-01 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catlin', '0005_auto_20190401_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='page_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
# Generated by Django 3.0.2 on 2020-02-12 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20200212_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approved',
            name='stay_approved',
            field=models.BooleanField(default=False, null=True, verbose_name='Approved'),
        ),
    ]

# Generated by Django 3.0.2 on 2020-02-06 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20200206_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='comment',
            field=models.CharField(max_length=10000, null=True, verbose_name='comment*'),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='date_applied',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='e-mail:'),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='firstname',
            field=models.CharField(max_length=100, null=True, verbose_name='first name*'),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='lastname',
            field=models.CharField(max_length=100, null=True, verbose_name='last name*'),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='num_of_ppl',
            field=models.CharField(choices=[('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four'), ('5', 'five'), ('6', 'six')], max_length=6, null=True),
        ),
    ]
# Generated by Django 3.2.9 on 2021-12-05 17:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departaments', '0005_alter_family_child'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departament',
            name='level',
        ),
        migrations.AddField(
            model_name='family',
            name='level',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(7)], verbose_name='level'),
        ),
    ]

# Generated by Django 3.2.9 on 2021-12-05 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departaments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='departaments.departament', verbose_name='child')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child', to='departaments.departament', verbose_name='parent')),
            ],
        ),
        migrations.AddField(
            model_name='departament',
            name='families',
            field=models.ManyToManyField(through='departaments.Family', to='departaments.Departament', verbose_name='families'),
        ),
    ]

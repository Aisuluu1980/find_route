# Generated by Django 3.1.13 on 2021-11-30 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0003_auto_20211130_0151'),
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traintest',
            name='from_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_city', to='cities.city', verbose_name='Из какого города'),
        ),
    ]

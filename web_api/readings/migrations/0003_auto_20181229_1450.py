# Generated by Django 2.1.4 on 2018-12-29 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0002_auto_20181229_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='readings', to='readings.Station'),
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-08 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0004_auto_20211008_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='averageeducationlevel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education_level', to='education.educationlevel'),
        ),
    ]

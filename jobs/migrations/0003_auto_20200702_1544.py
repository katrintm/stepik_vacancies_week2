# Generated by Django 3.0.7 on 2020-07-02 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20200701_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='vacancy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='jobs.Vacancy'),
        ),
    ]

# Generated by Django 3.2.5 on 2021-08-07 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210807_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.projectstatus'),
        ),
    ]

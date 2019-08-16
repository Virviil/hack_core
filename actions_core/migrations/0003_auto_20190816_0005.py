# Generated by Django 2.2.2 on 2019-08-15 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actions_core', '0002_remove_organization_q'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timelineentity',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='timelineentity',
            name='organization',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='actions_core.Organization'),
        ),
    ]
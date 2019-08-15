# Generated by Django 2.2.2 on 2019-08-15 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('logo_url', models.URLField()),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=250)),
                ('q', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aliah_date', models.DateField()),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1)),
                ('age', models.IntegerField()),
                ('marital_status', models.CharField(choices=[('s', 'Single'), ('m', 'Married')], max_length=1)),
                ('number_of_children', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TimelineEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('entity_type', models.CharField(choices=[('Right', 'r'), ('Suggestion', 's')], max_length=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('is_complited', models.BooleanField(default=False)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actions_core.Organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actions_core.User')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actions_core.User')),
            ],
        ),
    ]

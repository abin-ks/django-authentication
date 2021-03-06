# Generated by Django 4.0.1 on 2022-03-09 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_profile_card'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile_card',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profile_card',
            name='mobile',
        ),
        migrations.CreateModel(
            name='Pr_card',
            fields=[
                ('prid', models.AutoField(primary_key=True, serialize=False)),
                ('mobile', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.profile_card')),
            ],
        ),
    ]

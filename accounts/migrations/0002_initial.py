# Generated by Django 4.1.4 on 2022-12-25 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('admindash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admindash.course'),
        ),
    ]

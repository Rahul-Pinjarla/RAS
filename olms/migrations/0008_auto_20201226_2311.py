# Generated by Django 3.1.4 on 2020-12-26 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olms', '0007_auto_20201226_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='usertype',
            field=models.CharField(choices=[('student', 'Student'), ('admin', 'Admin'), ('care_taker', 'CareTaker'), ('security', 'Security')], default='student', max_length=10),
        ),
    ]
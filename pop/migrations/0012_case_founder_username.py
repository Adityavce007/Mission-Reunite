# Generated by Django 2.1.2 on 2018-10-25 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pop', '0011_case_founder_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='founder_username',
            field=models.CharField(max_length=30, null=True),
        ),
    ]

# Generated by Django 4.1 on 2022-09-13 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_link_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='visits',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

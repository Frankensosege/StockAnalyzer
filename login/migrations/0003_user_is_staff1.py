# Generated by Django 4.2 on 2023-04-14 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_remove_user_alias_remove_user_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff1',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 4.2 on 2024-04-30 06:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_alter_user_email_alter_user_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birthday",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="user",
            name="nickname",
            field=models.CharField(max_length=50),
        ),
    ]

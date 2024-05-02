# Generated by Django 4.2 on 2024-05-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0005_alter_user_birthday_alter_user_nickname"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("male", "남성"), ("female", "여성")],
                max_length=80,
                null=True,
            ),
        ),
    ]
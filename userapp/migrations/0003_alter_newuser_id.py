# Generated by Django 4.1.2 on 2022-11-13 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0002_rename_client_identity_id_newuser_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newuser",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
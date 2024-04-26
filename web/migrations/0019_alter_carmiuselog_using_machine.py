# Generated by Django 5.0.3 on 2024-04-23 16:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0018_remove_carmiinfo_carmi_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carmiuselog",
            name="using_machine",
            field=models.CharField(
                db_index=True,
                max_length=64,
                null=True,
                unique=True,
                verbose_name="使用机器",
            ),
        ),
    ]
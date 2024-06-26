# Generated by Django 5.0.3 on 2024-04-07 08:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0012_carmiinfo_generating_time_carmiinfo_generating_user_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="carmiinfo",
            name="generating_time",
        ),
        migrations.RemoveField(
            model_name="carmiinfo",
            name="generating_user",
        ),
        migrations.RemoveField(
            model_name="carmiinfo",
            name="using_machine",
        ),
        migrations.RemoveField(
            model_name="carmiinfo",
            name="using_time",
        ),
        migrations.RemoveField(
            model_name="carmiinfo",
            name="using_user",
        ),
        migrations.AlterField(
            model_name="carmiinfo",
            name="carmi_code",
            field=models.CharField(
                db_index=True, max_length=64, unique=True, verbose_name="卡密"
            ),
        ),
        migrations.CreateModel(
            name="CarmiGenLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "generating_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="生成时间"),
                ),
                (
                    "carmi_code",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="web.carmiinfo",
                        verbose_name="卡密",
                    ),
                ),
                (
                    "generating_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="web.userinfo",
                        verbose_name="生成用户",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CarmiUseLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "using_machine",
                    models.CharField(max_length=64, null=True, verbose_name="使用机器"),
                ),
                ("using_time", models.DateTimeField(null=True, verbose_name="使用时间")),
                ("due_time", models.DateTimeField(null=True, verbose_name="到期时间")),
                (
                    "carmi_code",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="web.carmiinfo",
                        verbose_name="卡密",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="UserSession",
        ),
    ]

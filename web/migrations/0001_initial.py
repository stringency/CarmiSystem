# Generated by Django 5.0.3 on 2024-03-31 08:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CarmiInfo",
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
                    "carmi_code",
                    models.CharField(db_index=True, max_length=64, verbose_name="卡密码"),
                ),
                ("carmi_duration", models.IntegerField(verbose_name="卡密时长")),
                ("carmi_status", models.IntegerField(default=0, verbose_name="卡密状态")),
            ],
        ),
        migrations.CreateModel(
            name="UserInfo",
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
                    "username",
                    models.CharField(db_index=True, max_length=32, verbose_name="用户名"),
                ),
                ("password", models.CharField(max_length=64, verbose_name="密码")),
                (
                    "token",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=64,
                        null=True,
                        verbose_name="TOKEN",
                    ),
                ),
                (
                    "role",
                    models.IntegerField(
                        choices=[(1, "管理员"), (2, "会员"), (3, "用户")],
                        default=3,
                        verbose_name="角色",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserSession",
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
                    "machine_code",
                    models.CharField(max_length=64, null=True, verbose_name="机器码"),
                ),
                ("valid_duration", models.IntegerField(default=0, verbose_name="有效时长")),
                (
                    "login_time",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="登录时刻"
                    ),
                ),
                (
                    "logout_time",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="离开时刻"
                    ),
                ),
                (
                    "login_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="web.userinfo",
                        verbose_name="登录用户",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CarmiLog",
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
                    "using_time",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="使用时间"
                    ),
                ),
                (
                    "carmi",
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
                (
                    "using_machine",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="web.usersession",
                        verbose_name="使用机器",
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-26 07:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0019_alter_carmiuselog_using_machine"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="role",
            field=models.IntegerField(
                choices=[(1, "管理员"), (2, "会员"), (3, "用户"), (4, "非法用户")],
                default=3,
                verbose_name="角色",
            ),
        ),
    ]
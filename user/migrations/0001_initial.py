# Generated by Django 3.2.13 on 2022-07-01 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dating_sex', models.CharField(choices=[('M', '男'), ('F', '女')], default='女', max_length=8, verbose_name='匹配的性别')),
                ('location', models.CharField(max_length=32, verbose_name='目标城市')),
                ('min_distance', models.IntegerField(default=1, verbose_name='最小查找范围')),
                ('max_distance', models.IntegerField(default=10, verbose_name='最大查找范围')),
                ('min_dating_age', models.IntegerField(default=18, verbose_name='最小交友年龄')),
                ('max_dating_age', models.IntegerField(default=45, verbose_name='最大交友年龄')),
                ('vibration', models.BooleanField(default=True, verbose_name='是否开启震动')),
                ('only_matche', models.BooleanField(default=True, verbose_name='不让为匹配的人看到我的相册')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=32, unique=True)),
                ('phonenum', models.CharField(max_length=16, unique=True)),
                ('sex', models.CharField(choices=[('M', '男'), ('F', '女')], max_length=8)),
                ('birth_year', models.IntegerField(default=2000)),
                ('birth_month', models.IntegerField(default=1)),
                ('birth_day', models.IntegerField(default=1)),
                ('avatar', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=64)),
            ],
        ),
    ]

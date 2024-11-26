# Generated by Django 3.0.6 on 2024-11-25 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardDetailsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='标题', max_length=255, unique=True, verbose_name='标题')),
                ('teamName', models.CharField(help_text='队伍名称', max_length=255, unique=True, verbose_name='队伍名称')),
                ('leader', models.CharField(help_text='负责人', max_length=255, verbose_name='负责人')),
                ('field', models.CharField(help_text='项目邻域', max_length=255, verbose_name='项目邻域')),
                ('needs', models.TextField(help_text='招募需求', max_length=255, verbose_name='招募需求')),
                ('memberCount', models.CharField(help_text='队伍规模', max_length=64, verbose_name='队伍规模')),
                ('CompetitionCategory', models.CharField(help_text='参与组别', max_length=16, verbose_name='参与组别')),
                ('description', models.TextField(verbose_name='项目描述')),
                ('history', models.TextField(verbose_name='历史成就')),
                ('creat_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '首页详情',
                'verbose_name_plural': '首页详情',
            },
        ),
    ]

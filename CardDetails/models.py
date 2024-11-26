from django.db import models
from django.conf import settings
from rest_framework.utils import json


class CardDetailsModel(models.Model):
    title = models.CharField(max_length=255,verbose_name='标题'
                            ,help_text='标题',unique=True)
    teamName = models.CharField(max_length=255,verbose_name='队伍名称',
                                    help_text='队伍名称',unique=True)
    leader = models.CharField(max_length=255, verbose_name='负责人',
                                help_text='负责人')
    field = models.CharField(max_length=255, verbose_name='项目邻域'
                             , help_text='项目邻域')
    needs = models.TextField(max_length=255, verbose_name='招募需求',
                                help_text='招募需求')
    memberCount = models.CharField(max_length=64, verbose_name='队伍规模',
                              help_text='队伍规模')
    CompetitionCategory = models.CharField(max_length=16, verbose_name='参与组别'
                             , help_text='参与组别')
    description = models.TextField(verbose_name='项目描述')
    history = models.TextField(verbose_name='历史成就')


    creat_at= models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True,verbose_name='更新时间')

    def set_description(self, description_list):
        self.description = json.dumps(description_list)

    def get_description(self):
        return json.loads(self.description)

    def set_history(self, history_list):
        self.history = json.dumps(history_list)

    def get_history(self,history_list):
        return json.loads(self.history)

    class Meta:
        verbose_name = '首页详情'
        verbose_name_plural = verbose_name #复数格式名称

    def __str__(self):  #当返回对象的字符串的时候，会调用这个方法，返回对象标题
        return self.title
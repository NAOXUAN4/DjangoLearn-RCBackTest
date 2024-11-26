from django.db import models
from django.conf import settings


class Course(models.Model):
    name = models.CharField(max_length=255,verbose_name='课程名称'
                            ,help_text='课程名称',unique=True)
    introduction = models.TextField(max_length=255,verbose_name='课程介绍',
                                    help_text='课程介绍',unique=True)
    price = models.DecimalField(max_digits=5,
                                decimal_places=2,verbose_name='课程价格')  # 5位整数，2位小数
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='老师',
                               help_text='老师',on_delete=models.CASCADE)  # 关联外键，user表的主键

    creat_at= models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True,verbose_name='更新时间')

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name #复数格式名称
        ordering = ('price',)   #查询对象时候的排序

    def __str__(self):  #当返回对象的字符串的时候，会调用这个方法，返回对象的名字
        return self.name
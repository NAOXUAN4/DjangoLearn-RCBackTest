from django.contrib import admin
from .models import CardDetailsModel



@admin.register(CardDetailsModel)  #注册数据模型装饰器
class CardDetailsAdmin(admin.ModelAdmin):
    list_display = ('title','teamName','leader','field',
                    'needs','memberCount','CompetitionCategory','description','history')
    search_fields = list_display  # 将列表显示设置为搜索字段，以便在管理界面中通过这些字段进行搜索
    list_filter = list_display    # 定义全部字段可以被删选
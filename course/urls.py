from django.urls import path,include
from course import views

urlpatterns = [
    # function based view---------------------------------
    path('fbv/list/',views.course_list, name = 'fbv-list'),
    path('fbv/detail/<int:pk>/',views.course_detail, name = 'fbv-detail'),

    # class based view-------------------------------------
    path('cbv/list/',views.CourseList.as_view(), name = 'cbv-list'),
    path('cbv/detail/<int:pk>/',views.CourseDetail.as_view(), name = 'cbv-detail'),

    # generic based view-----------------------------------
    path('gcbv/list/',views.CourseListGeneric.as_view(), name = 'gcbv-list'),
    path('gcbv/detail/<int:pk>/',views.CourseDetailGeneric.as_view(), name = 'gcbv-detail'),

    # viewsets --------------------------------------------
    path('vs/',views.CourseViewSet.as_view(
        {'get':'list',
         "post":"create"})),  #GET请求 使用list方法
    path('vs/<int:pk>/',views.CourseViewSet.as_view(
        {'get':'retrieve', #GET请求使用retrieve方法
         'put':'update', #PUT请求使用update方法
         'patch':'partial_update',  #PATCH请求使用partial_update方法
         'delete':'destroy'})),  #DELETE请求使用destroy方法
]

from rest_framework.response import Response
from .models import Course
from .serializer import CourseSerializer
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets


# 函数视图 （Function Based View）-----------------------------------------------------------------------------------------
@api_view(['GET','POST'])
def course_list(request):
    if request.method == 'GET':
        # 对Course模型进行序列化,many=True表示序列化多个
        s = CourseSerializer(instance = Course.objects.all(),many=True)
        #返回响应序列化后数据.data
        return Response(data = s.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        # 对POST请求数据序列化
        s = CourseSerializer(data=request.data) # partial=True表示部分字段更新
        if s.is_valid():  #校验合法性
            # 保存数据,指定teacher字段为当前post的用户
            s.save(teacher = request.user)
            return Response(data=s.data,status=status.HTTP_201_CREATED)
        return Response(data=s.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def course_detail(request,pk):
    """
    指定id修改
    :param request:
    :param pk: primary key
    :return:
    """
    try:   # 捕获异常，如果未找到对应数据表
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response({'message':'课程不存在'},status=status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'GET':  # 获取数据
            s = CourseSerializer(instance=course)
            return Response(data=s.data,status=status.HTTP_200_OK)
        elif request.method == 'PUT': #更新数据
            # 拿到数据先序列化 ，data：传入数据本体， instance：要修改的实例， partial：部分更新
            s = CourseSerializer(data=request.data,instance=course,partial=True)
            if s.is_valid():
                s.save()
                return Response(data=s.data,status=status.HTTP_200_OK)
        elif request.method == 'DELETE':  #删除
            course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

# 类视图（Class Based View） ---------------------------------------------------------------------------------------------

#getList类
class CourseList(APIView):
    def get(self, request):
        querySet = Course.objects.all()
        s = CourseSerializer(instance=querySet,many=True)
        return Response(data=s.data,status=status.HTTP_200_OK)

    def post(self, request):
        s = CourseSerializer(data=request.data)
        if s.is_valid():
            s.save(teacher = self.request.user)
            return Response(data=s.data,status=status.HTTP_201_CREATED)
        return Response(data=s.errors,status=status.HTTP_400_BAD_REQUEST)

#Detail类
class CourseDetail(APIView):
    def get_object(self,pk):   # 统一获取对象
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({'message':'课程不存在'},status=status.HTTP_404_NOT_FOUND)
    def get(self,request,pk):
        course = self.get_object(pk)
        s = CourseSerializer(instance=course)
        return Response(data=s.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        course = self.get_object(pk)
        s = CourseSerializer(data=request.data,instance=course,partial=True)
        if s.is_valid():
            s.save()
            return Response(data=s.data,status=status.HTTP_200_OK)
    def delete(self,request,pk):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 通用类视图（Generic Classed Based View） --------------------------------------------------------------------------------
class CourseListGeneric(generics.ListCreateAPIView): #继承自APIVIEW List方法
    queryset = Course.objects.all()    # 获取数据
    serializer_class = CourseSerializer  # 序列化器

    # 重写Mixin里面的create方法，用于修改值来自外键user的teacher字段
    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class CourseDetailGeneric(generics.RetrieveUpdateDestroyAPIView): #继承自RetrieveUpdateDestroyAPIView,同时有GET,PUT,DELETE
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

#视图集（ViewSets） ------------------------------------------------------------------------------------------------------
class CourseViewSet(viewsets.ModelViewSet):  #混合了通用类视图等方法
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)
from django.urls import path
from . import views

# 正在部署的应用名称

app_name = 'dict'

urlpatterns = [
    # path 函数将url映射到视图view
    # 接口1：访问全部字典
    path('word-list/',views.word_list,name = 'word_list'),
    path('word-detail/<int:id>/',views.word_detail,name = 'word_detail'),
    path('translate/',views.translate,name = 'translate'),
    path('search/',views.search,name = 'search'),
    path('deeplearning/',views.deeplearning,name = 'deeplearning'),
    path('insert/',views.insert,name = 'insert'),
    path('order/',views.order,name = 'order'),
]
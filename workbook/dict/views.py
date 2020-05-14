from django.shortcuts import render,redirect
from .models import Word,WordColumn
# 爬虫相关
import requests
import json
# 引入表单
from .forms import UserInputForm,UserInsert
# 引入分页模块
from django.core.paginator import Paginator
# 导入 HttpResponse 模块
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from . import models

# 单词列表
def word_list(request):
    # 取出所有的 word
    word_list = Word.objects.all()
    # 每页显示10个单词
    paginator = Paginator(word_list, 3)
    # 获取 url 中的页码
    page = request.GET.get('page')
    # 将相应的页码返回给words
    words = paginator.get_page(page)
    # 返回的对象做成字典
    context = {'words':words}
    # 载入模板 将 context返回
    return render(request,'word/list.html',context)

# 单词详情
def word_detail(request,id):
    # 提取出相应的单词
    word = Word.objects.get(id = id)
    # 需要传递给模板的对象
    context = {'word':word}
    # 返回
    return render(request,'word/detail.html',context)

# 翻译模块
def translate(request):
    # 提取用户提交得数据
    userInput = request.POST.get('userInput')
    print(userInput)

    if userInput is None:
        return render(request,'word/translate.html')
    else:
        # 爬虫代码
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        Form_data = {
            'i':'',
            'from':'AUTO',
            'to':'AUTO',
            'smartresult':'dict',
            'client':'fanyideskweb',
            'salt':'15893888011282',
            'sign':'2e7b48b2843fef18430425b7266e367d',
            'ts':'1589388801128',
            'bv':'0ea2f265e69dc7094ed5f0b64ef39e0b',
            'doctype':'json',
            'version':'2.1',
            'keyform':'fanyi.web',
            'action':'FY_BY_REALTlME'
        }
        Form_data['i']=str(userInput)

        response = requests.post(url,data = Form_data)
        youdaofanyi = json.loads(response.text)
        fanyi = youdaofanyi['translateResult'][0][0]['tgt']
        result = {}
        result['userInput']=userInput
        result['result']=fanyi
        context = {'result':result}
        print(context)
        return render(request,'word/translate.html',context)

def search(request):
    # 提取用户提交得数据
    userInput = request.POST.get('userInput')
    # print(userInput)
    if userInput is not None:
        searchResult = Word.objects.get(spell = str(userInput))
        # print(searchResult.example)
        context = {'userSearch':searchResult}
        return render(request,'word/search.html',context)
    else:
        return render(request,'word/search.html')

def deeplearning(request):
    # 取出所有的 word
    # try:
    #     word_list = WordColumn.objects.get(id=1)
    # except :
    #     print("查询失败")
    # 每页显示10个单词
    # paginator = Paginator(word_list, 3)
    # 获取 url 中的页码
    # page = request.GET.get('page')
    # 将相应的页码返回给words
    # words = paginator.get_page(page)
    # 返回的对象做成字典
    # context = {'words':words}
    # 载入模板 将 context返回
    return HttpResponse("暂不支持外键查询")

def insert(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = UserInsert(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new = article_post_form.save(commit=False)
            # 将新文章保存到数据库中
            new.save()
            # 完成后返回到文章列表
            return redirect('dict:word_list')
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = UserInsert()
        # 赋值上下文
        context = { 'article_post_form': article_post_form }
        # 返回模板
        return render(request, 'word/insert.html', context)

def order(request):
    # 取出所有的 word
    word_list = Word.objects.filter(spell__contains='b')
    # 每页显示10个单词
    paginator = Paginator(word_list, 3)
    # 获取 url 中的页码
    page = request.GET.get('page')
    # 将相应的页码返回给words
    words = paginator.get_page(page)
    # 返回的对象做成字典
    context = {'words':words}
    # 载入模板 将 context返回
    return render(request,'word/list.html',context)
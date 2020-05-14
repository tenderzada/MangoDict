from django.db import models
from django.utils import timezone

class WordColumn(models.Model):
    """
    单词的分类
    """
    # 分类标题
    title = models.CharField(max_length=100, blank=True)
    # 创建时间
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# 单词数据模型
class Word(models.Model):
    # 单词拼写,最长为100
    spell = models.CharField(max_length = 100)
    # 单词词性
    # nature = models.CharField(max_length = 10)
    # 过去式
    past = models.CharField(max_length = 100,default = '')
    # 过去分词
    pasted = models.CharField(max_length = 100,default = '')
    # 现在分词
    nowing = models.CharField(max_length = 100,default = '')
    # 名词复数
    fushu = models.CharField(max_length = 200,default = '')
    # 词性+翻译
    translation = models.CharField(max_length = 200,default = '')
    # 典型例句
    example = models.TextField()
    # 创建时间
    created = models.DateTimeField(default = timezone.now)
    # 修改时间
    # updated = models.DateTimeField(auto_now=True)

    # 单词与分类的 “一对多” 外键
    column = models.ForeignKey(
        WordColumn,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        # related_name='column'
    )
    
    # 内部类 class Meta
    class Meta:
        ordering = ('-created',)

    # 定义当前调用对象的__str__方法时候返回spell
    def __str__(self):
        return self.spell

# 用户提交的翻译内容
class UserInput(models.Model):
    # 用户提交的中文
    userInput = models.CharField(max_length = 100)


# 引入表单类
from django import forms
# 引入文章模型
from .models import UserInput,Word

# 用户提交的表单
class UserInputForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = UserInput
        # 定义表单包含的字段
        fields = ('userInput',)

# 用户搜索表单
# class UserSearchForm(forms.ModelForm):
#     class Meta:
#         model = UserSearch
#         fields = ('userInput',)

# 用户提交的新增
class UserInsert(forms.ModelForm):
    class Meta:
        model = Word
        fields = ('spell','past','pasted','nowing','fushu','translation','example',)
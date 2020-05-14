from django.contrib import admin

# Register your models here.

from .models import Word
from .models import WordColumn

# 注册Word到后台中
admin.site.register(Word)
admin.site.register(WordColumn)
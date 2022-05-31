from django.contrib import admin
from .models import Question, Choice

# Register your models here.

# 관리자 사이트에서 관리하고자 하는 테이블 추가(화면에 뿌려줌 -> CRUD 가능)
admin.site.register(Question)
admin.site.register(Choice)
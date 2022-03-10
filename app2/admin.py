from django.contrib import admin

# Register your models here.
from .models  import Grades,Students,Text
admin.site.register(Grades)
admin.site.register(Students)
# 账号Ana 182515131
admin.site.register(Text)
list_display = []
list_filter = []
search_fields = []
list_per_page = []
from django.contrib import admin
from .models import Article

# 이전에는 admin 설정이 project단에서 해주는거로 알고있었는데, 그게 아니라 각각의 app 내의 기능들을 추가해주는 것이었음!!!

# Register your models here.
admin.site.register(Article) # Article 클래스에 관한 권한을 등록해준다고 보면 됨!

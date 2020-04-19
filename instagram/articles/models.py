from django.db import models
# models 자체는 데이터를 관리하기 위해 사용!
# 그렇기 때문에 model class를 정의한 후에는 migrate 작업이 요구된다!

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    created_at = models.DateTimeField(auto_now = True)
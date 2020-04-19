from django import forms
from .models import Article

# model을 사용자들에게 보기좋게 만들어주기 위해 쓰는게 ModelForm!!! (선택사항이지만 안 할 필요는 없다.)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
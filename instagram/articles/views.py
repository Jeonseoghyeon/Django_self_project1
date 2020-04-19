from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# 밑의 내용들은

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request,'articles/index.html',context)

def detail(request,pk):
    article = Article.objects.get(pk=pk) # pk, id 둘 다 상관 없음(일단 지금 상황에서는 같음)
    context = {
        'article':article
    }
    return render(request,'articles/detail.html',context)

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form':form
    }
    return render(request,'articles/create.html',context)

def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk) # redirect를 위해 pk값을 같이 넘겨준다 !!!!!!!!!!!
    else:
        form = ArticleForm(instance=article) # instance : 기존에 있던 값을 넣어주는 것 ! 수정해야 하니까 !!
    context = {
        'form':form
    }
    return render(request,'articles/update.html',context)

def delete(request,pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

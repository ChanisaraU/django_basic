from django.shortcuts import render
from .models import articles
from django.http import HttpResponse
# Create your views here.
def article_list(request) :
    x = articles.objects.all().order_by('body')
    return render(request,"articles/articles_list.html", {'qq':x})
def article_detail(request, slugdetail) :
    return HttpResponse(slugdetail)
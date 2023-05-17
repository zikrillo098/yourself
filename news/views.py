from django.shortcuts import render
from django.views.generic import UpdateView, CreateView, ListView
from .models import *


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'article'

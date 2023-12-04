from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("article-create", views.ArticleCreateView.as_view(), name='article-create'),
    path("article/<slug:slug>", views.ArticleView.as_view(), name='article'),
    path("article/<slug:slug>/parse", views.ArticleParseView.as_view(), name='article-parse'),
    path("article/<slug:slug>/summarize", views.ArticleSummarizeView.as_view(), name='article-summarize'),
    path("article/<slug:slug>/reset-summary", views.ArticleResetSummaryView.as_view(), name='article-reset-summary'),
]


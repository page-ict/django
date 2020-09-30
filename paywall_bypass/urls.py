from django.urls import path
from . import  views
from django.views.generic import TemplateView

#urlpatterns = [
#    path('', views.index, name='index'),
#    path('post/', views.individual_post, name='individual_post'),
#]

from . import views
from django.urls import path

urlpatterns = [
    path('article/', views.ArticleView.as_view(), name='article'),

]
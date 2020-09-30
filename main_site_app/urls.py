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
    path('', views.PostListLimited.as_view(), name='home'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('blog/', views.BlogList.as_view(), name='blog'),
    path('projects/', views.ProjectList.as_view(), name='projects'),
    path('projects/<slug:slug>/', views.ProjectDetail.as_view(), name='project_detail'),
    path('resume/', views.ResumeList.as_view(), name='resume')
]
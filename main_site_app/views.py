from django.http import HttpResponse
from django.shortcuts import render
import json


#def index(request):
#    return HttpResponse('Hello, welcome to the index page.')

#def individual_post(request):
#    return HttpResponse('Hi, this is where an individual post will be.')

from django.views import generic
from .models import Post, Resume, Project, User

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    #tit = 'This is a test'
    #Post.objects.create(
    #    title= tit,
    #    slug = tit.replace(' ', '-'),
    #    author = User.objects.get(id=1),
    #    content = 'blah blah',
    #    status = 1
    #)
    #queryset = [tit]
    template_name = 'index_2.html'

class PostListLimited(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:2]
    template_name = 'index_2.html'

class BlogList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'project_detail.html'

class ResumeList(generic.ListView):
    queryset = Resume.objects.filter(status=1).order_by('-dob')
    #print(type(Resume.objects))


    template_name = 'resume.html'



class ProjectList(generic.ListView):
    queryset = Project.objects.filter(status=1).order_by('-created_on')
    template_name = 'projects.html'
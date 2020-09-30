from django.shortcuts import render
from .models import Article
from django.views import generic
import requests
from bs4 import BeautifulSoup
import urllib.parse

class ArticleView(generic.ListView):
    template_name = 'article.html'

    def create_article(self, url):
        r = requests.get(url, verify=False)
        x = r.text
        soup = BeautifulSoup(x)  # make soup that is parse-able by bs
        ps = soup.findAll('p')
        titles = soup.findAll('title')
        title = ''.join([z.text for z in titles])
        content = '\n\n'.join([p.text for p in ps])

        try:
            Article.objects.create(
                title= title,
                slug = title.replace(' ', '-'),
                author = 'Examiner',
                content = content,
            )

            status = True
        except:
            status = False

        return {'Status':status, 'Title':title}


    def get_queryset(self):
        try:
            examiner_url = urllib.parse.unquote(self.request.GET['url'])
            # print(examiner_url)
            status = self.create_article(examiner_url)

            if status['Status'] is True:
                queryset = Article.objects.order_by('-created_on')[:1]
            else:
                queryset = Article.objects.filter(title=status['Title'])[:1]


            return queryset

        except:
            queryset = []

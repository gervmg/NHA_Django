from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.http import HttpResponse
from django.template import loader

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def testing(request):
  template = loader.get_template('blog/test.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))            

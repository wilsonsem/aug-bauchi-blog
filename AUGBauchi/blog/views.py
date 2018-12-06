from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
	return render(request, 'blog/index.html', {})
def contact(request):
	return render(request, 'blog/contact.html', {})
def events(request):
	return render(request, 'blog/events.html', {})
def post1(request):
	return render(request, 'blog/post1.html', {})
def post2(request):
	return render(request, 'blog/post2.html', {})
def post3(request):
	return render(request, 'blog/post3.html', {})
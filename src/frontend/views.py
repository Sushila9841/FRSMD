from django.shortcuts import render
from django.views.generic import View


class HomePage(View):
    def get(self, request, *args, **kwargs):
         
        return render(request, 'frontend/index.html')
    
class About(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'frontend/about.html')
    
class Contact(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'frontend/contact.html')
    
class Blogs(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'frontend/blog.html')
    
class Blog(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'frontend/blog')
    
    
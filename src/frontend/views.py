from django.shortcuts import render
from django.views.generic import View
from predict.forms import CameraForm


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

        return render(request, 'frontend/blogs.html')
    
class Blog(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'frontend/blog')
    

class Camera(View):
    def get(self, request, *args, **kwargs):
        form = CameraForm()
        context = {
            'form': form
        }

        return render(request, 'frontend/camera.html', context)
    

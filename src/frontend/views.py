from django.shortcuts import render
from django.views.generic import View
from predict.forms import CameraForm
from django.http import HttpResponse


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
    
        return render(request, 'frontend/camera.html')
    
    def post(self, request, *args, **kwargs):
        # get image file image object from request.FILES
        captured_image_data = request.FILES.get('image_file')

        print(captured_image_data)

        return HttpResponse(captured_image_data)
        
from django.shortcuts import render
from django.views.generic import View
from predict.forms import CameraForm
from django.http import HttpResponse
from predict.mood_detect import detect_emotions
import numpy as np
import cv2
from blogs.models import Blog

class HomePage(View):
    def get(self, request, *args, **kwargs):
         
        return render(request, 'frontend/index.html')
    
class About(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'frontend/about.html')
    
class Contact(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'frontend/contact.html')
    
class BlogsView(View):
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        context = {
            'blogs': blogs
        }

        return render(request, 'frontend/blogs.html', context)
    
class BlogView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'frontend/blog')
    

class Camera(View):
    def get(self, request, *args, **kwargs):
    
        return render(request, 'frontend/camera.html')
    
    def post(self, request, *args, **kwargs):
        # get image file image object from request.FILES
        captured_image_data = request.FILES.get('image_file')
        if captured_image_data:
            # Read the image data from the uploaded file
            image_bytes = captured_image_data.read()

            # Convert the image data to a NumPy array
            nparr = np.frombuffer(image_bytes, np.uint8)

            # Decode the NumPy array to an OpenCV image
            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            # Perform emotion detection on the image
            moods = detect_emotions(image)

        print("Detected emotions:", moods)

        return HttpResponse('<h1>Detected emotions:{}</h1>'.format(moods))
        
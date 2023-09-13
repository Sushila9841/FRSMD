from django.shortcuts import render
from django.views.generic import View
from predict.forms import CameraForm
from django.http import HttpResponse
from predict.mood_detect import detect_emotions
import numpy as np
import cv2
from blogs.models import Blog
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from userprofile.mixin import LoginRequired
from django.contrib.auth.models import User
from userprofile.models import UserProfile
from predict.moods import Moods
from food.models import Food

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request,  'frontend/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(self.request, usr)
            return redirect('/camera')
        else:
            context = {
                "error": "incorrect credentials"
            }
            return render(request, 'frontend/login.html', context)
        
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
        
class SignUpView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'frontend/signup.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        age = int(request.POST["age"])
        phone = request.POST["phone"]
        address = request.POST["address"]
        user = User.objects.create_user(username=username, password=password)
        user.save()
        userprofile = UserProfile.objects.create(user=user, age=age, phone_number=phone, address=address)
        userprofile.save()  
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('/camera')
        return render(request, 'frontend/signup.html')

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
        pk = kwargs.get('pk')
        blog = Blog.objects.get(pk=pk)
        context = {
            'blog': blog
        }   
        return render(request, 'frontend/blog_single.html', context)
    

class Camera(LoginRequired, View):
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

        if 'Happy' in moods:
            foods = Food.objects.filter(food_category=Moods.happy)
        elif 'Sad' in moods:
            foods = Food.objects.filter(food_category=Moods.sad)
        elif 'Angry' in moods:
            foods = Food.objects.filter(food_category=Moods.angry)
        elif 'Surprise' in moods:
            foods = Food.objects.filter(food_category=Moods.surprise)
        elif 'Fear' in moods:
            foods = Food.objects.filter(food_category=Moods.fear)
        elif 'Disgust' in moods:
            foods = Food.objects.filter(food_category=Moods.disgust)
        else:
            foods = Food.objects.filter(food_category=Moods.neutral)

        print("Detected moods:", moods)

        context = {
            'foods': foods,
            'moods': moods
        }

        return render(request, 'frontend/food_suggest.html', context)
        
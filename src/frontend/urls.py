from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about', About.as_view(), name='about'),
    path('contact', Contact.as_view(), name='contact'),
    path('blogs', Blogs.as_view(), name='blogs'),
    path('blog/<int:pk>', Blog.as_view(), name='blog'),
    path('camera', Camera.as_view(), name='camera'),

]

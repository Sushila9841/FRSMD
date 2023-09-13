from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about', About.as_view(), name='about'),
    path('contact', Contact.as_view(), name='contact'),
    path('blogs', BlogsView.as_view(), name='blogs'),
    path('blog/<int:pk>', BlogView.as_view(), name='blog'),
    path('camera', Camera.as_view(), name='camera'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

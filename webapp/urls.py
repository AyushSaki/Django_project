from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('secret/',views.about,name='secret'),
    path('training/',views.training,name='training'),
    path('gallery/',views.gallery,name='gallery'),
    path('contact/',views.contact,name='contact'),
    path('register/',views.register,name='register'),
]
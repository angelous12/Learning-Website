from django.urls import path
from . import views
urlpatterns = [    
    path('',views.index , name='index'),
    path('About',views.about , name='about'),
    path('Contact',views.contact , name='contact'),
    path('Deatil-Course/<int:id>' , views.singlecourses , name='singlecourses'),
    path('All-Courses' , views.allcourses , name='allcourses'),     
    path('Blog' , views.blog , name='blog'),
    path('Single-Blog/<int:id>' , views.singleblog , name='singleblog'),
    path('Single-Post/<int:id>' , views.openpost , name='openpost'),

]
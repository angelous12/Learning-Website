from django.urls import path
from . import views
urlpatterns = [
    path('login',views.login , name='login'),
    path('logout',views.logout_form , name='logout'),
    path('Profile',views.myprofile , name='profile'),
    path('My-Courses',views.MyCourses , name='mycourse'),
    path('views-video/<int:id>', views.viewsvedio , name='viewsvedio'),
]
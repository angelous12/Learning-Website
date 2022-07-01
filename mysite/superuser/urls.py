from django.urls import path
from . import views
urlpatterns = [
    path('', views.indexsuper , name='indexsuper'),
    path('Review-Checkout/<int:id>' , views.editcheckoutsuper , name= 'editcheckoutsuper'),
    path('Delete-Review-Checkout/<int:id>' , views.deletecheckoutsuper , name= 'deletecheckoutsuper'),
    path('All-Category' , views.categorycoursesuper , name='categorycoursesuper'),
    path('Add-Category' , views.addcategorycoursesuper , name='addcategorycoursesuper'),
    path('Edit-Category/<int:id>' , views.editcategorycoursesuper , name='editcategorycoursesuper'),
    path('Delete-Category/<int:id>' , views.deletecategorycoursesuper , name='deletecategorycoursesuper'),       
    path('Add-Course/<int:id>' , views.addcoursecategorysuper , name='addcoursecategorysuper'),
    path('All-Course/<int:id>' , views.coursessuper , name='coursessuper'),
    path('Edit-Course/<int:id>' , views.editcoursesuper , name='editcoursesuper'),
    path('Delete-Course/<int:id>' , views.deletecoursesuper , name='deletecoursesuper'),
    path('Exams-Category/<int:id>' , views.examthiscategorysuper , name='examthiscategorysuper'),
    # path('Add-User-To-Course' , views.addusertocourse , name= 'addusertocourse'), 
    path('Add-Exam/<int:id>', views.addexamsuper , name='addexamsuper'),
    path('Add-Quiz/<int:id>', views.addquiz , name='addquiz'),
    path('All-Exam', views.allexamsuper , name='allexamsuper'),
    path('Delete-Exam/<int:id>' , views.deleteexamsuper , name='deleteexamsuper'),
    path('Edit-Exam/<int:id>' , views.editexamsuper , name='editexamsuper'),
    path('All-Question/<int:id>' , views.seequestionsuper , name='seequestionsuper'),
    path('Add-Exam', views.addexamonlysuper , name='addexamonlysuper'),
    path('Add-Answer-Exam/<int:id>', views.addanswersuper , name='addanswersuper'),
    path('See-Result-Exam/<int:id>', views.seeresultexamsuper , name='seeresultexamsuper'),
    path('Delete-Question/<int:id>' , views.deletequestionsuper , name='deletequestionsuper'),
    path('Edit-Question/<int:id>' , views.editquestionsuper , name='editquestionsuper'),    
    path('Delete-User/<int:id>' , views.deleteuseractivatesuper , name='deleteuseractivatesuper'),
    path('Edit-Profile',views.editprofilesuper , name='editprofilesuper'),
    path('change-password',views.changepasswordsuper,name='password_changesuper'),
    path('User-Activate',views.useractivatesuper,name='useractivatesuper'),
    path('User-Activate-Deatil/<int:id>',views.deatiluseractivatesuper,name='deatiluseractivatesuper'),
    path('User-Activate-Result/<int:id>',views.deatilexamactivatesuper,name='deatilexamactivatesuper'),
    path('User-Activate-Course/<int:id>',views.coursebuyuseractive,name='coursebuyuseractive'), 
    path('All-Category-Blog',views.categoryblogssuper,name='categoryblogssuper'),    
    path('Add-Category-Blog',views.addcategoryblogssuper,name='addcategoryblogssuper'), 
    path('Edit-Category-Blog/<int:id>',views.editcategoryblogssuper,name='editcategoryblogssuper'), 
    path('Delete-Category-Blog/<int:id>',views.deletecategoryblogssuper,name='deletecategoryblogssuper'),
    path('See-Blogs-Category/<int:id>',views.seepostblogthiscategorysuper,name='seepostblogthiscategorysuper'),
    path('Deatil-Blog/<int:id>',views.openpostblogsuper,name='openpostblogsuper'),
    path('Delete-Blog/<int:id>',views.deletepostblogsuper,name='deletepostblogsuper'),
    path('Info-Contact',views.infocontactsuper,name='infocontactsuper'),
    path('Edit-Info-Contact/<int:id>',views.editinfocontactsuper,name='editinfocontactsuper'),  
    path('All-Message' , views.messagecontactus , name='messagecontactus'),
    path('Edit-Message/<int:id>' , views.editmessagecontactus , name='editmessagecontactus'),
    path('delete-Message/<int:id>' , views.deletemessagecontactus , name='deletemessagecontactus'),  
    path('All-Reviews' , views.opinionssuper , name='opinionssuper'),
    path('Add-Reviews' , views.addopinionssuper , name='addopinionssuper'),
    path('Delete-Reviews/<int:id>' , views.deleteopinionssuper , name='deleteopinionssuper'),
]
from django.urls import path
from . import views
urlpatterns = [
    path('', views.student_exam_view , name='student_exam_view'),        
    path('start_exam_view/<int:id>', views.start_exam_view , name='start_exam_view'),
    path('calculate-marks', views.calculate_marks_view,name='calculate-marks'),
    path('Result-All', views.marksallexams , name='marksallexams'),
    path('Result-Exam/<int:id>', views.reviewexam , name='reviewexam'),
]
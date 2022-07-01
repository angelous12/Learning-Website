from django.db import models

# Create your models here.
from page.models import Category
from django.conf import settings


class Exam(models.Model):
    category = models.ForeignKey(Category , on_delete=models.CASCADE , blank=True)
    course_name = models.CharField(max_length=200)
    question_number = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Exam")
        verbose_name_plural = ("Exam")
        ordering = ['-create_at']

    def __str__(self):
        return self.course_name
    
    

class Question(models.Model):    
    course=models.ForeignKey(Exam,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField() 
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)    
    cat=(('ا','ا'),('ب','ب'),('ج','ج'),('د','د'))
    answer=models.CharField(max_length=200,choices=cat)

    class Meta:
        verbose_name = ("Question")
        verbose_name_plural = ("Question")

    def __str__(self):
        return self.question


class Result(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.student.username + ' |  marks = ' + str(self.marks) 
    
    
class AnswarExam(models.Model):
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    class Meta:
        verbose_name = ("Answar Exam")
        verbose_name_plural = ("Answar Exams")

    def __str__(self):
        return self.exam.course_name
    
class AnswarUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    course = models.ForeignKey(Exam,on_delete=models.CASCADE )
    question=models.CharField(max_length=600)
    answer = models.CharField(max_length=500)
    answeruser = models.CharField(max_length=500)
    marks = models.PositiveIntegerField()
    class Meta:
        verbose_name = ("Answar User")
        verbose_name_plural = ("Answar User")

    def __str__(self):
        return self.course.course_name

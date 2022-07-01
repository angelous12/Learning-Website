from dataclasses import fields
from django import forms
from accounts.models import UserCustom
#from quiz.models import Modules
from page.models import Category, CategoryBlog , Chekout, CommentBlog, ContactMessage, Courses, HomeOpinions, InfoContact, PostBlog
from quiz.models import AnswarExam, Exam, Question



class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = '__all__' 
		widgets = {
			'status':forms.Select(attrs={'class':'form-control'}),
   			'title':forms.TextInput(attrs={'class':'form-control'}),
			'deatil':forms.TextInput(attrs={'class':'form-control'}),
			'descrption':forms.TextInput(attrs={'class':'form-control'}),
			'image':forms.FileInput(attrs={'class':'form-control'}),
			'price':forms.NumberInput(attrs={'class':'form-control'}),			
		}
  
  
class ChekoutForm(forms.ModelForm):
	class Meta:
		model = Chekout
		fields = ('status',) 
		widgets = {
			'status':forms.Select(attrs={'class':'form-control'}),			
		}
  
  

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'
        widgets = {
            'category':forms.Select(attrs={'class':'form-control'}),
			'course_name':forms.TextInput(attrs={'class':'form-control'}),
			'question_number':forms.NumberInput(attrs={'class':'form-control'}),			
			'total_marks':forms.NumberInput(attrs={'class':'form-control'}),			
		}
        
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question','marks','option1','option2','option3','option4','answer')
        widgets = {
			'question':forms.TextInput(attrs={'class':'form-control'}),						
			'marks':forms.NumberInput(attrs={'class':'form-control'}),	
   			'option1':forms.TextInput(attrs={'class':'form-control'}),		
			'option2':forms.TextInput(attrs={'class':'form-control'}),
			'option3':forms.TextInput(attrs={'class':'form-control'}),
			'option4':forms.TextInput(attrs={'class':'form-control'}),
			'answer':forms.Select(attrs={'class':'form-control'}),	
		}
        
        
class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('course','question','marks','option1','option2','option3','option4','answer')
        widgets = {
            'course':forms.Select(attrs={'class':'form-control'}),
			'question':forms.TextInput(attrs={'class':'form-control'}),						
			'marks':forms.NumberInput(attrs={'class':'form-control'}),	
   			'option1':forms.TextInput(attrs={'class':'form-control'}),		
			'option2':forms.TextInput(attrs={'class':'form-control'}),
			'option3':forms.TextInput(attrs={'class':'form-control'}),
			'option4':forms.TextInput(attrs={'class':'form-control'}),
			'answer':forms.Select(attrs={'class':'form-control'}),	
		}



class UserForm(forms.ModelForm):
    class Meta:
        model = UserCustom
        fields = ('first_name','last_name','username','email','last_login',)
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),            
            'username':forms.TextInput(attrs={'class':'form-control'}),   
            'email':forms.TextInput(attrs={'class':'form-control',}),              
            'last_login':forms.TextInput(attrs={'class':'form-control'}),                           
        }
        

        
class CoursesForm(forms.ModelForm):
	class Meta:
		model = Courses
		fields = ('title','image','link' , 'status')
		widgets = {
			'title':forms.TextInput(attrs={'class':'form-control'}),
			'status':forms.Select(attrs={'class':'form-control'}),                       
			'link':forms.TextInput(attrs={'class':'form-control'}),               
			'image':forms.FileInput(attrs={'class':'form-control'}),                
		}    
        
        
class CategoryBlogForm(forms.ModelForm):
    class Meta:
        model = CategoryBlog
        fields = '__all__'
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),                                  
        }
        
        
class PostBlogForm(forms.ModelForm):
    class Meta:
        model = PostBlog
        fields = ('deatil',)
        widgets = {            
            'deatil':forms.Textarea(attrs={'class':'form-control'}),                                  
        }
        
class CommentBlogForm(forms.ModelForm):
    class Meta:
        model = CommentBlog
        fields = ('comment','image',)
        widgets = {            
            'comment':forms.Textarea(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),                                  
        }
        
class AnswerExamForm(forms.ModelForm):
    class Meta:
        model = AnswarExam
        fields = '__all__'
        widgets = {            
            'exam':forms.Select(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),                                  
        }
        
        
class InfoContactForm(forms.ModelForm):
    class Meta:
        model = InfoContact
        fields = '__all__'
        widgets = {
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'fax':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'facebook':forms.TextInput(attrs={'class':'form-control'}),
            'twiiter':forms.TextInput(attrs={'class':'form-control'}),
            'youtube':forms.TextInput(attrs={'class':'form-control'}),

        }
        
        
class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__'
        widgets = {
            'status': forms.Select(attrs={'class':'form-control'}),
            'note':forms.TextInput(attrs={'class':'form-control'}),       
            'name':forms.TextInput(attrs={'class':'form-control'}),            
            'email': forms.TextInput(attrs={'class':'form-control'}),             
            'message':forms.TextInput(attrs={'class':'form-control'}),                          

        }
        
class HomeOpinionsForm(forms.ModelForm):
    class Meta:
        model = HomeOpinions
        fields = '__all__'
        widgets = {
            'image': forms.FileInput(attrs={'class':'form-control'}),                            

        }     

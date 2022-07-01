import ssl
from unicodedata import category
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from page.models import Category, Chekout
from quiz.models import AnswarExam, AnswarUser, Exam, Question, Result
from accounts.models import UserCustom
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
# Create your views here.

@login_required(login_url='/user/login')
@allowed_users(allowed_roles=['customr'])
def student_exam_view(request):  
    get_user = UserCustom.objects.get(id = request.user.id)
    test = get_user.category.all()
    exam = Exam.objects.filter(category__in = test)
    context = {
        'courses':exam
    }
    
    return render(request,'accounts/user-exams.html'  , context)
#accounts/user-exams.html





        
@login_required(login_url='/user/login')  
@allowed_users(allowed_roles=['customr'])         
def start_exam_view(request,id):
    course= Exam.objects.get(id=id)    
    verfied = Chekout.objects.filter(user_id = request.user.id , category = course.category , status = 'Confirm')
    if verfied :    
        result = Result.objects.filter(student_id=request.user.id, exam = course)      
        if result:
            get_result = Result.objects.get(student_id = request.user.id , exam_id = course.id)
            # print(get_result.id)            
            return redirect('/quiz/Result-Exam/'+str(get_result.id))
        else:
            questions= Question.objects.all().filter(course=course)
            if request.method=='POST':
                pass
            test = list(questions.values())
            #return JsonResponse(test, safe=False)
            #return print(questions)
            create = Result.objects.create(student_id = request.user.id , exam=course , marks=0)
            response= render(request,'accounts/start-exam.html',{'course':course,'questions':questions })
            response.set_cookie('course_id',course.id)
            return response
    else:
        return JsonResponse({'msg':'Please buy category to buy Exam'})


@login_required(login_url='/user/login')
@allowed_users(allowed_roles=['customr'])
def calculate_marks_view(request):
    if request.method=='POST':
        pass
    if request.COOKIES.get('course_id') is not None:
        course_id = request.COOKIES.get('course_id')
        course= Exam.objects.get(id=course_id)
        # return JsonResponse({'xx':request.COOKIES})
        total_marks=0
        markfirst = 0
        zero = 0
        questions= Question.objects.all().filter(course=course)
        for i in range(len(questions)):            
            selected_ans = request.COOKIES.get('qs_'+str(i+1))
            answeruser = AnswarUser()
            answeruser.user_id = request.user.id
            answeruser.course = course
            answeruser.answeruser = selected_ans
            answeruser.question = questions[i].question          
            actual_answer = questions[i].answer
            answeruser.answer = actual_answer
            if answeruser.answeruser == answeruser.answer:
                markfirst += questions[i].marks
                answeruser.marks = markfirst
                answeruser.save()
            else:
                answeruser.marks = zero
                answeruser.save()
            if selected_ans == actual_answer:
                # HttpResponseRedirect('student_exam_view')
                total_marks = total_marks + questions[i].marks                                                                              
        student =  UserCustom.objects.get(id=request.user.id)
        result = Result.objects.get(student_id = student , exam = course )
        result.marks=total_marks        
        result.save()
        return redirect('student_exam_view')
    else:
        return JsonResponse({'msg':'hh'})

 
@login_required(login_url='/user/login')
@allowed_users(allowed_roles=['customr'])
def marksallexams(request):
    get_exams = Result.objects.filter(student_id = request.user.id)
    context = {
        'get_exams':get_exams,
    }
    return render(request,'accounts/resultall.html', context)
 
 
@login_required(login_url='/user/login')
@allowed_users(allowed_roles=['customr'])
def reviewexam(request , id):        
    get_exam = Result.objects.get(id=id)
    answeruser = AnswarUser.objects.filter(user_id = request.user.id , course_id = get_exam.exam.id)   
    answerexam = AnswarExam.objects.get(exam = get_exam.exam)       
    context = {
        'get_exam':get_exam,
        'answeruser':answeruser,
        'answerexam':answerexam,
    }        
    return render(request,'accounts/single-result.html', context)
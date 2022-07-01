from email import message
from django.shortcuts import get_object_or_404, redirect, render
from page.models import Category, CategoryBlog , Chekout, CommentBlog, ContactMessage, Courses, InfoContact, PostBlog,HomeOpinions
from quiz.models import AnswarExam, Exam, Question, Result
from .forms import AnswerExamForm, CategoryBlogForm, CategoryForm, ChekoutForm, CommentBlogForm, ContactMessageForm, CoursesForm, ExamForm, HomeOpinionsForm, InfoContactForm, PostBlogForm, QuestionForm, QuestionsForm, UserForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import update_session_auth_hash
from accounts.models import UserCustom
from accounts.decorators import admin_only
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/user/login')
@admin_only
def indexsuper(request): 
    users = UserCustom.objects.all().count()
    totalcourses = Category.objects.filter(status = 'True').count()
    totalsales = Chekout.objects.filter(status = 'Confirm')
    totalsaless = 0
    for totalsales in totalsales:
        totalsaless += totalsales.total
    checkout = Chekout.objects.all().order_by('-id')
    checkoutcomplete = Chekout.objects.filter(status = 'Confirm').order_by('-id')
    checkoutpending = Chekout.objects.filter(status = 'Pending').order_by('-id')
    checkoutcancelled = Chekout.objects.filter(status = 'Canceled').order_by('-id')
    context = {
        'checkout':checkout,
        'checkoutcomplete':checkoutcomplete,
        'checkoutpending':checkoutpending,
        'checkoutcancelled':checkoutcancelled,
        'users':users,
        'totalcourses':totalcourses,
        'totalsaless':totalsaless,
    }
    return render (request , 'homesuper/indexsuper.html' , context)

@login_required(login_url='/user/login')
@admin_only
def editcheckoutsuper(request , id):
    if request.user.is_staff:      
        get_id = Chekout.objects.get(id=id)
        if request.method == 'POST':
            form = ChekoutForm(request.POST , instance=get_id)
            if form.is_valid():
                form.save()
                if get_id.status == 'Confirm':
                    add_category = UserCustom.objects.get(id = get_id.user.id)
                    add_category.category.add(get_id.category)
                    add_category.activeuser = True
                    add_category.save()
                if get_id.status == 'Canceled':
                    add_category = UserCustom.objects.get(id = get_id.user.id)
                    add_category.category.remove(get_id.category)                    
                    if add_category.category.all().count() == 0:                                            
                        add_category.activeuser = False
                        add_category.save()
                    else:                        
                        add_category.activeuser = True                        
                        add_category.save()
            return redirect ('indexsuper')
        else:
            form = ChekoutForm(instance=get_id)
        context = {
            'form':form,
            'get_id':get_id
        }
        return render(request , 'homesuper/checkoutsuper.html',context)
 
 
@login_required(login_url='/user/login')
@admin_only               
def deletecheckoutsuper(request , id):
    if request.user.is_staff:        
        get_id = Chekout.objects.get(id=id)
        get_id.delete()
        return redirect ('indexsuper')
                     
@login_required(login_url='/user/login')
@admin_only          
def categorycoursesuper(request):
    categoryall  = Category.objects.all().order_by('-id')  
    name = None 
    if 'categorysearch' in request.GET:
        name = request.GET['categorysearch']
        if name:
            categoryall = categoryall.filter(title__icontains=name)
    categoryfalse = Category.objects.filter(status = False).order_by('-id')
    context = {
        'categoryall':categoryall,        
        'categoryfalse':categoryfalse,
    }
    return render (request , 'homesuper/allcategorysuper.html',context)

@login_required(login_url='/user/login')
@admin_only
def addcoursecategorysuper(request , id):
    getcategory = Category.objects.get(id=id)
    if 'back' in request.POST:
        data = request.POST
        course_title = data['title']
        link = data['link']        
        image = request.FILES.get('image')
        course = Courses.objects.create(
            category_id = id,
            title = course_title,
            image = image,
            link = link,
            status = True,
        )
        return redirect('categorycoursesuper')
    if 'see' in request.POST:
        data = request.POST
        course_title = data['title']
        link = data['link']        
        image = request.FILES.get('image')
        course = Courses.objects.create(
            category_id = id,
            title = course_title,
            image = image,
            link = link,
            status = True,
        )
        return redirect('/dashboard/All-Course/'+str(getcategory.id))
    context = {
        'getcategory':getcategory
    }       
    return render(request , 'homesuper/addcoursesuper.html', context)
    
@login_required(login_url='/user/login')
@admin_only
def coursessuper(request , id):
    getcategory = Category.objects.get(id=id)
    filtercourse = Courses.objects.filter(category_id = getcategory.id )
    #print(filtercourse)
    context = {
        'course':filtercourse,
        'examget':getcategory
    }
    return render(request , 'homesuper/seecoursesuper.html', context)


def addhomeworkcourse(request,id):
    pass


@login_required(login_url='/user/login')
@admin_only
def editcoursesuper(request , id):
    url = request.META.get('HTTP_REFERER')
    get_id = Courses.objects.get(id=id)
    if request.method == 'POST':
        form = CoursesForm(request.POST , request.FILES , instance=get_id)
        if form.is_valid():
            form.save()
            return redirect ('/dashboard/All-Course/'+str(get_id.category.id))
    else:
        form = CoursesForm(instance=get_id)
    context = {
        'form':form,
        'get_id':get_id,
    }
    return render (request , 'homesuper/editcoursesuper.html' , context)



@login_required(login_url='/user/login')
@admin_only
def examthiscategorysuper(request , id):
    get_id = Category.objects.get(id=id)
    exam_filter = Exam.objects.filter(category_id = get_id.id)    
    context = {
        'exam':exam_filter,
        'get_id':get_id,
    }
    return render (request , 'homesuper/examthiscategorysuper.html' , context)
    
    
@login_required(login_url='/user/login')
@admin_only
def deletecoursesuper(request,id):
    url = request.META.get('HTTP_REFERER')
    if request.user.is_staff:
        get_id = Courses.objects.get(id=id)
        get_id.delete()
        return HttpResponseRedirect (url)
        

@login_required(login_url='/user/login')
@admin_only
def editcategorycoursesuper(request , id):
    get_id = Category.objects.get(id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST , request.FILES , instance=get_id)
        if form.is_valid():
            form.save()
            return redirect('categorycoursesuper')
    else:
        form = CategoryForm(instance=get_id)
    context = {
        'form':form,
        'get_id':get_id
    }
    return render(request , 'homesuper/editcategorysuper.html' , context)



@login_required(login_url='/user/login')
@admin_only
def addcategorycoursesuper(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = CategoryForm(request.POST , request.FILES)
            if form.is_valid():
                form.save()
                return redirect('categorycoursesuper')
        else:
            form = CategoryForm()
        context = {
            'form':form
        }
        return render(request , 'homesuper/addcategorysuper.html', context)



@login_required(login_url='/user/login')
@admin_only   
def deletecategorycoursesuper(request,id):    
    if request.user.is_staff:
        get_id = Category.objects.get(id=id)
        get_id.delete()
        return redirect('categorycoursesuper')


@login_required(login_url='/user/login')
@admin_only
def addexamsuper(request , id):
    getcategory = Category.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        exam_name = data['nameexam']
        questionnumber = data['numberq']
        totalmarks = data['marks']
        exam = Exam.objects.create(
            category_id = id,
            course_name = exam_name,
            question_number = questionnumber,
            total_marks = totalmarks,
        )
        return redirect('/dashboard/Add-Quiz/'+str(exam.id))
    context = {
        'getcategory':getcategory
    }       
    return render(request , 'homesuper/addexamsuper.html', context)



@login_required(login_url='/user/login')
@admin_only
def addquiz(request , id):
    getid = Exam.objects.get(id=id)
    url = request.META.get('HTTP_REFERER')
    if 'add' in request.POST:
        data = request.POST
        question = data['question']
        marks = data['marks']
        option1 = data['option1'] 
        option2 = data['option2'] 
        option3 = data['option3'] 
        option4 = data['option4'] 
        answar  = data['answar'] 
        save = Question.objects.create(
            course_id = id,
            marks = marks,
            question = question,
            option1 = option1,
            option2 = option2,
            option3 = option3,
            option4 = option4,
            answer = answar,
        )
        return HttpResponseRedirect (url)
    if 'back' in request.POST:
        data = request.POST
        question = data['question']
        marks = data['marks']
        option1 = data['option1'] 
        option2 = data['option2'] 
        option3 = data['option3'] 
        option4 = data['option4'] 
        answar  = data['answar'] 
        save = Question.objects.create(
            course_id = id,
            marks = marks,
            question = question,
            option1 = option1,
            option2 = option2,
            option3 = option3,
            option4 = option4,
            answer = answar,
        )
        return redirect ('/dashboard/All-Question/'+str(save.course.id))
    context = {
        'getid':getid
    }
    return render(request , 'homesuper/addquestionsuper.html',context)




#Exam && Question 


@login_required(login_url='/user/login')
@admin_only
def allexamsuper(request):
    if request.user.is_staff:
        allexam = Exam.objects.all().order_by('-id')
        name = None 
        if 'examsearch' in request.GET:
            name = request.GET['examsearch']
            if name:
                allexam = allexam.filter(course_name__icontains=name)
        context = {
            'allexam':allexam,
        }
        return render(request , 'homesuper/allexamsuper.html' , context)
  
@login_required(login_url='/user/login')
@admin_only
def addanswersuper(request , id):
    get_id = Exam.objects.get(id=id)
    getanswer = AnswarExam.objects.filter(exam_id = id).count()
    # print(getanswer)
    if getanswer == 1:
        edit = AnswarExam.objects.get(exam_id = id)    
        if request.method == 'POST':  
            form = AnswerExamForm(request.POST , request.FILES  , instance=edit ) 
            if form.is_valid():
                form.save()     
                return redirect('allexamsuper')
        else:
            form = AnswerExamForm(instance=edit )
        context = {
            'form':form,
            'get_id':get_id,
            'getanswer':edit,
        }
        return render(request , 'homesuper/addanswersuper.html' ,context)
    elif getanswer == 0:
        get_name_exam = Exam.objects.get(id=id)
        if request.method == 'POST':
            image =  request.FILES.get('image')
            add_new = AnswarExam.objects.create(
                exam_id = id,
                image = image
            )
            return redirect('allexamsuper')
        context = {
            'get_name_exam':get_name_exam,
        }
        return render(request , 'homesuper/addaanswersuper.html' , context )
    else:
        return JsonResponse({'msg':'The Count Answer == 1 please Edit Not Add More'})  
    
    
      
@login_required(login_url='/user/login')
@admin_only    
def addexamonlysuper(request):
    if request.user.is_staff: 
        if request.method == 'POST':
            form = ExamForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('allexamsuper')
        else:
            form = ExamForm()
        context = {
            'form':form
        }
        return render(request , 'homesuper/addexamonlysuper.html' , context)  
    
    
    
@login_required(login_url='/user/login')
@admin_only 
def deleteexamsuper(request,id):
    if request.user.is_staff:
        get_id = Exam.objects.get(id=id)
        get_id.delete()
        return redirect('allexamsuper')




@login_required(login_url='/user/login')
@admin_only
def editexamsuper(request , id):
    get_id = Exam.objects.get(id=id)
    if request.method == 'POST':
        form = ExamForm(request.POST , instance=get_id)
        if form.is_valid():
            form.save()
            return redirect('allexamsuper')
    else:
        form = ExamForm(instance=get_id)
    context = {
        'form':form,      
    }
    return render(request , 'homesuper/editexamsuper.html' , context)

@login_required(login_url='/user/login')
@admin_only
def seeresultexamsuper(request , id):
    get_id = Exam.objects.get(id=id)
    result = Result.objects.filter(exam = get_id)
    resultcount = Result.objects.filter(exam = get_id).count()
    checkout = Chekout.objects.filter(category = get_id.category , status= 'Confirm').count() 
    checkouts = Chekout.objects.filter(category = get_id.category , status= 'Confirm') 
      
    context = {
        'get_id':get_id,
        'result':result,        
    }
    return render(request , 'homesuper/seeresultexamsuper.html' , context)
    
    
    
    
@login_required(login_url='/user/login')
@admin_only
def seequestionsuper(request , id):
    if request.user.is_staff:
        examget = Exam.objects.get(id=id)
        question = Question.objects.filter(course_id = id)
        context = {
            'question':question,
            'examget':examget,
        }
        return render(request , 'homesuper/allquestionsuper.html' , context)
    
    
@login_required(login_url='/user/login')
@admin_only  
def deletequestionsuper(request , id):
    url = request.META.get('HTTP_REFERER')
    if request.user.is_staff:
        getid = Question.objects.get(id=id)
        getid.delete()
        return HttpResponseRedirect (url)
    
    
@login_required(login_url='/user/login')
@admin_only  
def editquestionsuper(request , id):
    get_id = Question.objects.get(id=id)
    if request.method == 'POST':
        form = QuestionsForm(request.POST , instance=get_id)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/All-Question/'+str(get_id.course.id))
    else:
        form = QuestionsForm(instance=get_id)
    context = {
        'form':form, 
        'get_id':get_id     
    }
    return render(request , 'homesuper/editquestionsuper.html' , context)

    

@login_required(login_url='/user/login')
@admin_only
def useractivatesuper(request):
    active = UserCustom.objects.filter(activeuser = True)    
    name = None
    if 'usersearch' in request.GET:
        name = request.GET['usersearch']
        if name:
            active = active.filter(username__icontains=name)
    context = {
        'user_buy':active,
    }
    return render(request , 'homesuper/useractivatesuper.html' , context)


@login_required(login_url='/user/login')
@admin_only
def deatiluseractivatesuper(request , id):
    get_id = UserCustom.objects.get(id=id)    
    context = {
        'userprofile':get_id
    }
    return render(request , 'homesuper/deatiluseractivatesuper.html' , context)

@login_required(login_url='/user/login')
@admin_only
def deatilexamactivatesuper(request , id):
    get_id = UserCustom.objects.get(id=id)
    result = Result.objects.filter(student = get_id )
    context = {
        'result':result,
        'get_id':get_id
    }
    return render(request , 'homesuper/deatilexamactivatesuper.html' , context)


@login_required(login_url='/user/login')
@admin_only
def coursebuyuseractive(request , id):
    get_id = UserCustom.objects.get(id=id)
    checkout = Chekout.objects.filter(user_id = get_id.id , status = 'Confirm')
    context = {
        'get_id':get_id,
        'checkout':checkout,
    }
    return render(request , 'homesuper/deatilcourseactivatesuper.html' , context)
    
    
    
@login_required(login_url='/user/login')
@admin_only   
def deleteuseractivatesuper(request,id):
    if request.user.is_staff:
        user = UserCustom.objects.get(id=id)        
        user.delete()
        return redirect('useractivatesuper')


@login_required(login_url='/user/login')
@admin_only
def editprofilesuper(request):   
    info = InfoContact.objects.first() 
    current_user = request.user    
    userinformation = UserCustom.objects.get(id=current_user.id)
    Userinfo = UserCustom.objects.get(id = current_user.id)
    if request.method == 'POST':
        userform = UserForm(request.POST , instance=userinformation)
        #userprfoile = UserForm(request.POST , instance=Userinfo)
        if userform.is_valid():
            userform.save()           
            return redirect ('editprofilesuper')
    else:
        userform = UserForm(instance=userinformation)
    if request.method == 'POST':
        userprfoile = UserForm(request.POST , instance=Userinfo)
        if userprfoile.is_valid():
            userprfoile.save()
            return redirect ('editprofilesuper')
    else:
        #userform = UserForm(instance=userinformation)
        userprfoile = UserForm(instance=Userinfo)
    #contant = InfoContact.objects.all().last()
    context = {
        'form':userform,
        'userprfoile':userprfoile,
        'Userinfo':Userinfo,
        'contant':info,
    }
    return render (request , 'homesuper/editprofilesuper.html',context)



@login_required(login_url='/user/login')
@admin_only
def changepasswordsuper(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        current = request.POST['cpwd']
        new_pas = request.POST['npwd']            
        user = UserCustom.objects.get(id=request.user.id)
        check = user.check_password(current)
        if check == True:
            user.set_password(new_pas)
            user.save()
            update_session_auth_hash(request, user)
            return JsonResponse ({'msg':'don'})
    #        messages.success(request , 'Your password is change! ')
            return HttpResponseRedirect(url)
    #     else:
    # #        messages.error(request , 'Your password is wrong, try again ')       
    return render(request , 'homesuper/change-passwordsuper.html')




# Blog 

@login_required(login_url='/user/login')
@admin_only
def categoryblogssuper(request):
    categoryall = CategoryBlog.objects.all()
    context = {
        'categoryall':categoryall
    }
    return render(request , 'homesuper/categoryblogssuper.html' , context)


@login_required(login_url='/user/login')
@admin_only
def addcategoryblogssuper(request):
    if request.method == 'POST':
        form = CategoryBlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoryblogssuper')
    else:
        form = CategoryBlogForm()
    context = {
        'form':form
    }
    return render(request , 'homesuper/addcategoryblogssuper.html' , context)
 
 
@login_required(login_url='/user/login')
@admin_only   
def editcategoryblogssuper(request , id):
    get_id = CategoryBlog.objects.get(id=id)
    if request.method == 'POST':
        form = CategoryBlogForm(request.POST , instance=get_id)
        if form.is_valid():
            form.save()
            return redirect('categoryblogssuper')
    else:
        form = CategoryBlogForm(instance=get_id)
    context = {
        'form':form,
        'get_id':get_id,
    }
    return render(request , 'homesuper/editcategoryblogssuper.html' , context)


@login_required(login_url='/user/login')
@admin_only
def deletecategoryblogssuper(request , id):
    if request.user.is_staff:
        get_id = CategoryBlog.objects.get(id=id)
        get_id.delete()
        return redirect('categoryblogssuper')
    


@login_required(login_url='/user/login')
@admin_only   
def seepostblogthiscategorysuper(request , id):
    get_id = CategoryBlog.objects.get(id=id)
    postblogpending = PostBlog.objects.filter(category_id = get_id.id , status = 'Pending')        
    postbloganswer = PostBlog.objects.filter(category_id = get_id.id , status = 'Answer')   
    context = {
        'get_id':get_id,
        'postblogpending':postblogpending,
        'postbloganswer':postbloganswer,        
    }
    return render(request , 'homesuper/seepostblogthiscategorysuper.html' , context)


@login_required(login_url='/user/login')
@admin_only
def openpostblogsuper(request , id):
    get_id = PostBlog.objects.get(id=id)
    checked =  CommentBlog.objects.filter(post_id = id ).count()
    status = 0
    if checked == 0 :
        if  request.method == 'POST':   
            form = PostBlogForm(request.POST , instance=get_id)           
            data = request.POST
            comment = data['comment']              
            image = request.FILES.get('image')
            commentblog = CommentBlog.objects.create(
                post_id = id,
                comment = comment,
                image = image,
            )
            get_id.status = 'Answer'
            get_id.save()
            if form.is_valid():                    
                form.save()
                return redirect('/dashboard/See-Blogs-Category/'+str(get_id.category.id))
        else:
            form = PostBlogForm(instance=get_id)            
        context = {        
        'form':form,
        'get_id':get_id,       
        }
    if checked == 1 :
        status = 1
        get_data =  CommentBlog.objects.get(post_id = id )
        # print(get_data.comment)
        if request.method == 'POST':            
            form_don = CommentBlogForm(request.POST, request.FILES , instance=get_data ) 
            if form_don.is_valid():
                form_don.save()
                return redirect('/dashboard/See-Blogs-Category/'+str(get_id.category.id))
        else:
            form_don = CommentBlogForm(instance=get_data)     
        context = {
            'form_don':form_don,
            'get_id':get_id,
            'get_data':get_data,
            'status':status,
        }            
    return render(request , 'homesuper/openpostblogsuper.html' , context)

@login_required(login_url='/user/login')
@admin_only
def deletepostblogsuper(request , id):
    url = request.META.get('HTTP_REFERER')
    get_id = PostBlog.objects.get(id=id)
    get_id.delete()
    return HttpResponseRedirect(url)




@login_required(login_url='/user/login')
@admin_only
def infocontactsuper(request):
    info = InfoContact.objects.all()
    context = {
        'info':info,
    }
    return render (request , 'homesuper/infocontactsuper.html' , context)


@login_required(login_url='/user/login')
@admin_only
def editinfocontactsuper(request,id):
    info_id = InfoContact.objects.get(id=id)
    if request.method == 'POST':
        editinfo = InfoContactForm(request.POST , instance=info_id)
        if editinfo.is_valid():
            editinfo.save()
            return redirect ('infocontactsuper')
    else:
        editinfo = InfoContactForm( instance=info_id)
    context = {
        'form':editinfo,
    }
    return render (request , 'homesuper/editinfocontactsuper.html' , context)


@login_required(login_url='/user/login')    
@admin_only
def messagecontactus(request):
    search = ContactMessage.objects.all()
    name = None
    if 'message' in request.GET:
        name = request.GET['message']   
        if name:
            search = search.filter(name__icontains = name)     
    contactread = ContactMessage.objects.filter(status = 'Read')
    contactclose = ContactMessage.objects.filter(status = 'Closed')
    context = {
        'contact':search,
        'contactread':contactread,
        'contactclose':contactclose,
    }
    return render (request , 'homesuper/contactussuper.html' , context)



@login_required(login_url='/user/login')    
@admin_only
def editmessagecontactus(request , id):
    contact = ContactMessage.objects.get(id=id)
    if request.method == 'POST':
        contactform = ContactMessageForm(request.POST , instance=contact)
        if contactform.is_valid():
            contactform.save()
            return redirect ('messagecontactus')
    else:
        contactform = ContactMessageForm(instance=contact)
    context = {
        'form':contactform
    }
    return render (request , 'homesuper/editcontactussuper.html' , context)


@login_required(login_url='/user/login')    
@admin_only
def deletemessagecontactus(request , id):
    contact = ContactMessage.objects.get(id=id)
    contact.delete()
    return redirect ('messagecontactus')



@login_required(login_url='/user/login')    
@admin_only
def opinionssuper(request):
    opinions = HomeOpinions.objects.all()
    context = {
        'opinions':opinions,
    }
    return render (request , 'homesuper/opinionssuper.html' , context)

@login_required(login_url='/user/login')    
@admin_only
def addopinionssuper(request):           
    if request.method == 'POST':
        form = HomeOpinionsForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()  
            if 'more' in request.POST:
                return redirect('addopinionssuper')   
            else:
                return redirect('opinionssuper')
    else:
        form = HomeOpinionsForm()
    context = {
        'form':form,
    }
    return render (request , 'homesuper/addopinionssuper.html' , context)

@login_required(login_url='/user/login')    
@admin_only
def deleteopinionssuper(request , id):
    get_id = HomeOpinions.objects.get(id=id)
    get_id.delete()
    return redirect('opinionssuper')





from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import requests
from django.contrib import messages
from django.contrib.auth import logout
import re
from django.contrib.auth.models import Group
from accounts.decorators import allowed_users
from page.models import Category, Chekout, Courses
from .models import UserCustom
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import login as authlogin
# Create your views here.



def login(request):
    if request.user.is_authenticated:
        return redirect ('/')
    else: 
        url = request.META.get('HTTP_REFERER')
        if 'login' in  request.POST :
            username = request.POST['username']
            password = request.POST['password']
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret':settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response':recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=data)
            result = r.json()
            if result['success']:  
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    authlogin(request, user)
                    return redirect('/')
                else:
                    messages.error(request , 'username & password is wrong')
                    return HttpResponseRedirect (url)
            else:
                messages.error(request , 'Recaptcha Error !')
                return redirect ('login')
                # Return an 'invalid login' error message.           
        if 'signup' in request.POST:            
            username = None
            firstname = None
            lastname = None            
            phone  = None
            # phonefather  = None
            email     = None
            password  = None
            if 'username' in request.POST : username = request.POST['username']
            else : messages.error(request , 'error in username')
            
            if 'firstname' in request.POST : firstname = request.POST['firstname']
            else : messages.error(request , 'error in firstname')
                     
            if 'lastname' in request.POST : lastname = request.POST['lastname']
            else : messages.error(request , 'error in lastname')
            
            
            if 'phone' in request.POST : phone = request.POST['phone']
            else : messages.error(request , 'error in phone')
            
            
            # if 'phonefather' in request.POST : phonefather = request.POST['phonefather']
            # else : messages.error(request , 'error in phonefather')
                                   

            if 'email' in request.POST : email = request.POST['email']
            else : messages.error(request , 'error email')


            if 'password' in request.POST : password = request.POST['password']
            else: messages.error(request , 'error password')

            #check value 

            if username and firstname and lastname and phone  and email  and password:
                #check the user name 
                if UserCustom.objects.filter(username=username).exists():
                        messages.error(request , 'The user name is taken')
                else:
                    if UserCustom.objects.filter(email=email).exists():
                        messages.error(request , 'The Email is taken')
                    else:
                        patt = "^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
                        if re.match(patt,email):
                            recaptcha_response = request.POST.get('g-recaptcha-response')
                            data = {
                            'secret':settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                            'response':recaptcha_response
                            }
                            r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=data)
                            result = r.json()
                            if result['success']:  
                                user = UserCustom.objects.create_user(email=email,
                                username=username , password=password, first_name=firstname , last_name=lastname , phone_number=phone,
                                phone_father=1)
                                user.save()
                                group = Group.objects.get(name='customr')
                                user.groups.add(group)
                                # group = Group.objects.get(name='customr')
                                # user.groups.add(group)                                
                                messages.success(request, 'Your Account is Created')
                                return redirect ('login')
                            else:
                                messages.error(request , 'Recaptcha Error !')
                                return redirect ('login')
                        else:
                            messages.error(request , 'The Email is Not Vaild')
            else:
                messages.error(request , 'Check Empty Fields')
    return render(request , 'accounts/login.html')

@login_required(login_url='/user/login')
def logout_form(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/user/login')  
@allowed_users(allowed_roles=['customr'])
def myprofile(request):
    get_user = UserCustom.objects.get(id = request.user.id )
    allsales = Chekout.objects.filter(user_id = get_user , status = 'Confirm')
    context = {
        'user':get_user,
        'allsales': allsales
    }
    return render(request , 'accounts/user-profile.html',context)
  
@login_required(login_url='/user/login')  
@allowed_users(allowed_roles=['customr'])
def MyCourses(request):
    get_user = UserCustom.objects.get(id = request.user.id )
    allsales = Chekout.objects.filter(user_id = get_user , status = 'Confirm')
    active = False
    if allsales:
        active = True
        CATID = request.GET.get('category')
        if CATID:  
            course = Courses.objects.filter(category_id = CATID)
            show_accounts = Chekout.objects.filter(user_id = get_user , category_id = CATID , status='Confirm')
            get_id = Category.objects.get(id=CATID)
            if show_accounts:
                contexts = {            
                    'course':course,
                    'get_id':get_id,
                }
                return render (request, 'courses/allcoursesthiscategory.html', contexts)
            else:
                return JsonResponse({'msg':'Please Buy'})
        else:
            context = {
                'allsales': allsales
            }
            return render(request , 'accounts/my-buy.html',context)
    else:       
       return render(request , 'accounts/my-buy.html')    
  
    
@login_required(login_url='/user/login')  
@allowed_users(allowed_roles=['customr']) 
def viewsvedio(request , id):
    course_id = Courses.objects.get(pk=id)
    show_accounts = Chekout.objects.filter(user_id = request.user.id , category = course_id.category , status='Confirm')
    if show_accounts:
        context = {
            'course_id':course_id
        }
        return render(request, 'accounts/viewscourse.html', context)
    else:
        return JsonResponse({'msg':' Please Buy'})
    
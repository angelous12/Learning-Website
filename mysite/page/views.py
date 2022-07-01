from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils.crypto import get_random_string
from page.models import Category, CategoryBlog, Chekout, CommentBlog, ContactMessage, Courses, HomeOpinions, PostBlog
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.decorators import allowed_users


@login_required(login_url='/user/login')
@allowed_users(allowed_roles=['customr'])
def contact(request):
    if request.method == 'POST':
        data = request.POST
        name = data['name']
        name2 = data['name2']
        email = data['email']
        message = data ['message']
        create = ContactMessage.objects.create(
            name = name + name2,
            email = email,
            message = message,        
        )
        messages.success(request , 'Message Sent success!!')                        
        return redirect ('contact')
    return render(request , 'home/contact.html' )

@login_required(login_url='/user/login')
@allowed_users(allowed_roles=['customr'])
def about(request):
    return render(request , 'home/about.html' )

@login_required(login_url='/user/login')
@allowed_users(allowed_roles=['customr'])
def index(request):
    random = Category.objects.filter(status = 'True').order_by('?')[:3]  
    opinion = HomeOpinions.objects.all()
    context = {
        'random':random,
        'opinion':opinion,
    }
    return render(request , 'home/index.html' , context)

@login_required(login_url='/user/login')
@allowed_users(allowed_roles=['customr'])
def singlecourses(request , id):
    get_id = Category.objects.get(id=id)
    checkk = False
    check = Chekout.objects.filter(user_id = request.user.id , status = 'Confirm' , category_id = id)
    if check:
        checkk = True
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        checkout = Chekout.objects.create(
            category_id = id,
            user_id = request.user.id,
            total = get_id.price,
            code = get_random_string(8).upper(),
            phone_number = request.POST['phone'],            
        )
        messages.success(request,'success sent please wait')
        return HttpResponseRedirect(url)        
    context = {
        'get_id':get_id,
        'checkk':checkk
    }
    return render(request , 'courses/single.html' , context)



@login_required(login_url='/user/login')
@allowed_users(allowed_roles=['customr'])
def allcourses(request):
    category = Category.objects.filter(status = 'True').order_by('-id')
    context  = {
        'cat':category
    }
    return render(request , 'courses/courses.html' , context)


@login_required(login_url='/user/login')
@allowed_users(allowed_roles=['customr'])
def blog(request):
    categories = CategoryBlog.objects.all()  
    if request.method == 'POST':                      
        data = request.POST
        image = request.FILES.get('image')
        category = CategoryBlog.objects.get(id=data['category'])        
        title = data['title']
        detail = data['detail']
        check = Chekout.objects.filter(user_id = request.user.id , status = 'Confirm') 
        if check: 
            create = PostBlog.objects.create(
                category = category,
                image = image,
                title = title,
                deatil = detail,
                user_id = request.user.id
            )
            get_catageory = create.category
            if get_catageory:
                get_cat_in_data_base = CategoryBlog.objects.get(title = get_catageory)
                get_cat_in_data_base.amount += 1
                get_cat_in_data_base.save()
                messages.success(request , 'create post don')             
                return redirect('blog') 
            else:
                messages.error(request , 'Error Please Try Again')  
                return redirect('blog') 
        else:
            messages.error(request , 'You Dont Have Any Course Buy !! Please Buy And Try Again')  
            return redirect('blog') 
                  
    context = {
        'cat':categories,
    }
    return render(request , 'blog/community.html' , context)
 
 
@login_required(login_url='/user/login')
@allowed_users(allowed_roles=['customr'])
def singleblog(request , id):
    get_id = CategoryBlog.objects.get(id=id)    
    filter = PostBlog.objects.filter(category_id = get_id.id)    
    context = {
        'get_id':get_id,
        'filter':filter,
    }
    return render(request , 'blog/onecategory.html' , context)

@login_required(login_url='/user/login')
@allowed_users(allowed_roles=['customr'])
def openpost(request , id):
    get_post = PostBlog.objects.get(id=id)
    if get_post.status == 'Answer':
        get_comment = CommentBlog.objects.get(post_id = id)
        # print(get_comment)
        if get_comment:        
            context = {
                'get_post':get_post,
                'get_comment':get_comment,
            }
    else:
        context = {
            'get_post':get_post,        
        }
    return render(request , 'blog/single-qu.html' , context)
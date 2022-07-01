from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from django.conf import settings

# Create your models here.

    
class HomeOpinions(models.Model):
    image = models.ImageField(upload_to='images/')   
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Opinions")
        verbose_name_plural = ("Opinions")
        ordering = ['-create_at']  
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
    
    


class Category(models.Model):
    STATUS = (
        #متاح
        ('True','True'),
        #غير متاح
        ('False','False'),
    )
    title = models.CharField(max_length=200 , blank=True)
    deatil = models.CharField(max_length=200, blank=True)
    descrption = RichTextUploadingField()
    image = models.ImageField(upload_to='images/')
    status = models.CharField(max_length=50 , choices=STATUS)
    price = models.FloatField(blank=True)    
    # create_at = models.DateTimeField(auto_now_add=True)
    # update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Category")
        # ordering = ['-create_at']

    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
    
    
class Courses(models.Model):
    STATUS = (
        #متاح
        ('True','True'),
        #غير متاح
        ('False','False'),
    )
    category = models.ForeignKey(Category , on_delete=models.CASCADE , blank=True)
    title = models.CharField(max_length=30 , blank=True)
    image = models.ImageField(upload_to='images/')
    link = models.CharField(max_length=500)
    status = models.CharField(max_length=50 , choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)    
    class Meta:
        verbose_name = ("Courses")
        verbose_name_plural = ("Courses")

    def __str__(self):
        return self.title
    
    
    
class Chekout(models.Model):
    STATUS = (    
        ('Confirm','Confirm'),    
        ('Pending','Pending'),
        ('Canceled','Canceled'),
    )
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    total = models.FloatField(blank=True)
    code = models.CharField(max_length=100 , blank= True)
    phone_number = models.CharField(max_length=100 , blank=True)
    status = models.CharField(max_length=50 , choices=STATUS , default= 'Pending')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = ("chekout")
        verbose_name_plural = ("chekout")

    def __str__(self):
        return self.user.username
    
    
    
class CategoryBlog(models.Model):
    title = models.CharField(max_length=200)
    amount = models.IntegerField(blank=True , default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
class PostBlog(models.Model):
    STATUS = ( 
        ('Pending','Pending'),
        ('Answer','Answer'),
    )
    category = models.ForeignKey(CategoryBlog , related_name='blog', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    deatil = models.TextField(max_length=200)    
    image = models.ImageField(upload_to='images/')
    status = models.CharField(max_length=50 , choices=STATUS , default= 'Pending')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("PostBlog")
        verbose_name_plural = ("PostBlogs")

    def __str__(self):
        return self.title


class CommentBlog(models.Model):
    post = models.ForeignKey(PostBlog , on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/' , blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("CommentBlog")
        verbose_name_plural = ("CommentBlog")

    def __str__(self):
        return self.post.title  




class InfoContact(models.Model):
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50 , blank=True)
    twiiter = models.CharField(max_length=50,blank=True )
    youtube = models.CharField(max_length=50 , blank=True)
    

    class Meta:
        verbose_name = ("InfoContact")
        verbose_name_plural = ("InfoContact")

    def __str__(self):
        return self.phone


class ContactMessage(models.Model):
    STATUS = (
        ('New','New'), 
        ('Read','Read'),
        ('Closed','Closed'),
    )
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True )    
    message = models.TextField(max_length=300, blank=True )
    status = models.CharField(max_length=10 , choices=STATUS , default='New')    
    note = models.CharField(max_length=50, blank=True )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = ("Contact Message")
        verbose_name_plural = ("Contact Message")

    def __str__(self):
        return self.name
    


from django.contrib import admin

from .models import CategoryBlog, CommentBlog, ContactMessage, Courses, HomeOpinions ,  InfoContact ,  Category , Chekout, PostBlog
# Register your models here.


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name','create_at','update_at', 'status']
    readonly_fields = ['name','email','message']
    list_filter = ['status']
    
    
admin.site.register(ContactMessage,ContactMessageAdmin)
admin.site.register(InfoContact)
admin.site.register(Category )
admin.site.register(HomeOpinions)
admin.site.register(Chekout)
admin.site.register(Courses)
admin.site.register(CategoryBlog)
admin.site.register(PostBlog)
admin.site.register(CommentBlog)


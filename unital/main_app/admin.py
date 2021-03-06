from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    def name(obj):
        return "%s %s" % (obj.first_name, obj.last_name)
    list_display = ('id', 'username', name, 'user_type', 'department', 'college', 'email')
    list_filter = ('user_type', 'college', 'department', 'session')
    fields = ('first_name', 
              'last_name',
              'father_name', 
              'username', 
              'password', 
              'email',
              'profile_pic', 
              'user_type', 
              'college',
              'graduation_programme',
              'department',
              'session',
              'gender', 
              'phone_no', 
              'dob', 
              'address' )
    list_display_links = ('id', 'username')
    search_fields = ('username', 'first_name')
    list_per_page = 25
    def save_model(self, request, obj, form, change):
        password = str(obj.password)
        if(password and len(password)<20):
            obj.set_password(password)
        super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)
admin.site.register(Notice)
admin.site.register(College)
admin.site.register(Department)
admin.site.register(CollegePictures)
admin.site.register(CollegeNotice)
admin.site.register(Syllabus)
admin.site.register(Notes)
admin.site.register(Subject)

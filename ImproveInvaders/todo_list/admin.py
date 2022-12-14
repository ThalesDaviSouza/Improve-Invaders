from django.contrib import admin
from .models import UserType, Sala, Task, StudentWork, EnrolledCourses
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserTypeInLine(admin.StackedInline):
    model = UserType
    can_delete = False
    verbose_name_plural = 'UsersTypes'


class CustomizeUserAdmin (UserAdmin):
    inlines = (UserTypeInLine, )



admin.site.register(Sala)
admin.site.register(Task)
admin.site.register(StudentWork)
admin.site.register(EnrolledCourses)
admin.site.unregister(User)
admin.site.register(User, CustomizeUserAdmin)


from django.contrib import admin
import re
from vote_teacher.models import Subject, Teacher, User
from vote_teacher.forms import UserForm


# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'create_date', 'is_hot')
    ordering = ('no', )


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'detail', 'good_count', 'bad_count',
                    'subject', 'photo')
    ordering = ('subject', 'no')

class UserAdmin(admin.ModelAdmin):
    list_display = ('no', 'username', 'password')
    ordering = ('no', )
    form = UserForm
    list_per_page = 10


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(User, UserAdmin)

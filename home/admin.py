from django.contrib import admin
from .models import Attendance, Semester, SubjectGrade, Fee, PersonalDetails

# Register your models here.
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'present','absent')
    list_filter = ('date', 'present','absent')
    search_fields = ('user__username', 'date')

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('user', 'semester_number', 'cgpa')
    list_filter = ('semester_number', 'cgpa')
    search_fields = ('user__username', 'semester_number')

@admin.register(SubjectGrade)
class SubjectGradeAdmin(admin.ModelAdmin):
    list_display = ('semester', 'subject_name', 'grade')
    list_filter = ('semester', 'grade')
    search_fields = ('semester__user__username', 'subject_name')

@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ('tuition_fee', 'hostel_fee', 'transport_fee', 'total_amount', 'paid_amount')
    list_filter = ('total_amount', 'paid_amount')
    search_fields = ('user__username',)

@admin.register(PersonalDetails)
class PersonalDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'valid_email', 'date_of_birth', 'address', 'department_of_btech', 'parent_name', 'mother_name')
    list_filter = ('department_of_btech',)
    search_fields = ('user__username', 'full_name', 'valid_email', 'parent_name', 'mother_name')

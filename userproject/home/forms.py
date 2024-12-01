# home/forms.py

from django import forms
from .models import Attendance, Semester, Fee, PersonalDetails

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['user', 'date', 'present','absent']

class ResultForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['user', 'semester_number', 'cgpa']


class FeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = ['tuition_fee', 'hostel_fee', 'transport_fee', 'total_amount', 'paid_amount']


class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = ['user', 'full_name', 'valid_email', 'date_of_birth', 'address', 'department_of_btech', 'parent_name', 'mother_name']

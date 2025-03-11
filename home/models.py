from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField()
    absent = models.BooleanField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"


class Semester(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    semester_number = models.PositiveIntegerField()
    cgpa = models.FloatField()

class SubjectGrade(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100)
    grade = models.CharField(max_length=2)


class Fee(models.Model):
    tuition_fee = models.DecimalField(max_digits=8, decimal_places=2)
    hostel_fee = models.DecimalField(max_digits=8, decimal_places=2)
    transport_fee = models.DecimalField(max_digits=8, decimal_places=2)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Fee Details for Tuition: {self.tuition_fee}, Hostel: {self.hostel_fee}, Transport: {self.transport_fee}"


class PersonalDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    valid_email = models.EmailField()
    date_of_birth = models.DateField()
    address = models.TextField()
    department_of_btech = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)






import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from .tokens import generate_token
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.hashers import make_password
from django.conf import settings
from .models import Attendance, Semester, SubjectGrade, Fee, PersonalDetails
from django.contrib.auth.decorators import login_required
from .forms import AttendanceForm, ResultForm, FeeForm, PersonalDetailsForm  # Ensure correct import here
from .models import Attendance, Semester, Fee, PersonalDetails

def home1(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'About.html')
def Faculty(request):
    return render(request, 'Faculty.html')
def Grievence(request):
    return render(request, 'Grievence.html')
def Syllabus(request):
    return render(request, 'Syllabus.html')

# for admin perspective
def registerAdmin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        hashed_password = make_password(password)
        my_user = User.objects.create_superuser(username=username, password=password)
        my_user.is_active = True
        my_user.save()
        return redirect('/login')
    return render(request, "admin_register.html")

def admin_dashboard(request):
    return redirect("/admin")

def formSubmission(request):
    if request.method == "POST":
        
        my_user = Student(
        )
        my_user.save()
        messages.success(request, "Data inserted successfully!")
        return redirect('/home')
    else:
        return render(request, 'home.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        hashed_password = make_password(password)
        print(username, password)
        # Check if user has entered correct credentials
        my_user = authenticate(username=username, password=password)
        if my_user is not None:
            # A backend authenticated the credentials
            login(request, my_user)
            if my_user.is_staff:
                return redirect("/adminpage")
            else:
                return redirect("/homepage")
        # No backend authenticated the credentials
        return render(request, 'login.html')
    return render(request, 'login.html')


def registerUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        
        hashed_password = make_password(password)
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username")
            return redirect('/register')
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('/register')
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
        if password != password2:
            messages.error(request, "Passwords didn't match")
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('/register')
                           
        my_user = User.objects.create_user(username=username, email=email, password=password)
        my_user.is_active = False
        my_user.save()
        messages.success(request, 'Account created successfully! We have sent you a confirmation email, please confirm your email in order to activate your account.')

        # Welcome mail
        subject = "Welcome to Django Login!"
        message = "Hello " + my_user.username + "!!\n" + "Welcome to Student Portal\n Thank you for visiting our website\n We have also sent to you a confirmation email, Now confirm your email then  yow will login by using with link..\n\n Thanking You\n  SANJEEVU SAI KUMAR" 
        from_email = settings.EMAIL_HOST_USER
        to_list = [my_user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Email Address Confirmation email
        current_site = get_current_site(request)
        email_subject = "Confirmation email from student portal !!"
        message2 = render_to_string('email_confirmation.html', {
            'name': my_user.first_name,
            'domain': get_current_site(request).domain,
            'uid': urlsafe_base64_encode(force_bytes(my_user.pk)),
            'token': generate_token.make_token(my_user),
            "protocol": 'https' if request.is_secure() else 'http'
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [my_user.email],
        )
        email.fail_silently = True
        email.send()
        return redirect('/login')
    
    return render(request, "admin_register.html")
        
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        my_user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        my_user = None

    if my_user is not None and generate_token.check_token(my_user, token):
        my_user.is_active = True
        my_user.save()
        messages.success(request, "Thank you for email confirmation. Now you can login your account.")
        login(request, my_user)
        return redirect('/login')
    else:
        return render(request, 'activation_failed.html')

def send_email():
    subject = 'Registration Verification'
    message = 'You have successfully registered in student portal and now you will login.'
    from_email = 'studentportalstudent462@gmail.com'  # Sender's email address (must be in EMAIL_HOST_USER)
    recipient_list = ['recipient@example.com']  # List of recipient(s) email addresses
    send_mail(subject, message, from_email, recipient_list)

# this is for after student login  the below data displayed 
@login_required
def attendance_list(request):
    # Filter attendances for the logged-in user
    attendances = Attendance.objects.filter(user=request.user)
    return render(request, 'attendance_list.html', {'attendances': attendances})


@login_required
def result_view(request):
    semesters = Semester.objects.filter(user=request.user)
    
    context = {
        'semesters': semesters
    }
    return render(request, 'result.html', context)

from .models import Fee
from .forms import FeeForm
@login_required
def fee_detail(request):
    fee = Fee.objects.first()  # Assuming there is only one fee instance for demonstration
    context = {
        'fee': fee,
    }
    return render(request, 'fee.html', context)

def fee_update(request):
    fee = Fee.objects.first()  # Assuming there is only one fee instance for demonstration

    if request.method == 'POST':
        form = FeeForm(request.POST, instance=fee)
        if form.is_valid():
            form.save()
            return redirect('fee_detail')
    else:
        form = FeeForm(instance=fee)

    context = {
        'form': form,
    }
    return render(request, 'fee_update.html', context)

@login_required
def personal_details_view(request):
    try:
        personal_details = PersonalDetails.objects.get(user=request.user)
    except PersonalDetails.DoesNotExist:
        personal_details = None
    
    if request.method == 'POST':
        form = PersonalDetailsForm(request.POST, instance=personal_details)
        if form.is_valid():
            form.save()
            messages.success(request, 'Personal details updated successfully.')
            return redirect('personal_details_view')
    else:
        form = PersonalDetailsForm(instance=personal_details)
    
    context = {
        'form': form,
        'personal_details': personal_details
    }
    return render(request, 'personal_details.html', context)





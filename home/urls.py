from django.contrib import admin
from django.urls import path 
from home import views


urlpatterns = [
    path('homepage',views.home,name="home"),
    path('home',views.formSubmission,name="home"),
    path('login',views.loginUser,name="login"),
    path('adminpage',views.admin_dashboard,name="admin"),
    path('register',views.registerUser,name="register"),
    path('admin_register',views.registerAdmin,name="admin_register"),
    path('activate/<uidb64>/<token>',views.activate,name="activate"),
    path('home1',views.home1,name="home1"),
    path('',views.home1,name="home1"),
    path('result/', views.result_view, name='result_view'),
    path('personal_details/', views.personal_details_view, name='personal_details_view'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('fee/', views.fee_detail, name='fee_detail'),
    path('fee_update/', views.fee_update, name='fee_update'),
    path('About/',views.about,name="about"),
    path('Faculty/',views.Faculty,name="Faculty"),
    path('Grievence/',views.Grievence,name="Grievence"),
    path('Syllabus/',views.Syllabus,name="Syllabus"),
]
    
    
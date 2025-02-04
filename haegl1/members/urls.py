from . import views
from django.urls import path

urlpatterns = [
 path('members/', views.members, name='members'),
 path('members_data/',views.members_data, name='members_data'),
 path('datapush/',views.datapush, name='datapush'),
 path('register/', views.register, name='register'),
 path('login/', views.user_login, name='login'),
 path('logout/', views.user_logout, name='logout'),
 path('dashboard/', views.userdashboard, name='dashboard'),
 path('login_dash/', views.dashboard_login, name='dashboard_login'),
 path('studentdashboard/',views.studentdashboard,name="studentdashboard"),
 path('staffregister/',views.staffregister,name="staffregister"),
 path('staffdashboard/',views.staff_dashboard,name="staffdashboard"),
 path('admindashboard/',views.admin_dashboard,name="admindashboard"),
 path('pr/',views.pr,name="pages_register"),
 ]

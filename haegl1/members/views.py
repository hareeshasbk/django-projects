from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template import loader
from .models import EmployeeInfo,EmployeeDetails
from django.contrib.auth.decorators import login_required


def members_data(request):
   mymembers=EmployeeInfo.objects.all().values()
   template=loader.get_template('members_data.html')
   context={
      'mymembers':mymembers,
   }
   return HttpResponse(template.render(context,request))


def datapush(request):
   if request.method=='POST':
      firstname=request.POST.get('firstname')
      lastname=request.POST.get('lastname')
      x=EmployeeInfo.objects.create(firstname=firstname,lastname=lastname)
      return redirect('members_data')

   return render(request,'datapush.html')


def register(request):
      if request.method == 'POST':
         firstname = request.POST.get('firstname')
         lastname = request.POST.get('lastname')
         username = request.POST.get('username')
         password = request.POST.get('password')
         email = request.POST.get('email')
         user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username, email=email, password=password)
         return redirect('members_data')
      else:
         return render(request, 'register.html')
      
# def user_login(request):
#    if request.method == 'POST':
#       username = request.POST.get('username')
#       password = request.POST.get('password')
#       user = authenticate(request,username=username, password=password)
#       if user is not None:
#          login(request, user)
#          # check superuser
#          if user.is_superuser:
#             return redirect('admindashboard') #redirect admin dashboard
#          elif user.is_active:
#             return redirect('members_data') #redirect staff dashboard
#          else:
#             context={'error_message':'Invalid username or password.'}
#             return render(request,'login.html',context)
#    return render(request,'login.html')

def user_login(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request,username=username, password=password)
      if user is not None:
         login(request, user)
         # check superuser
         if user.is_superuser:
            return redirect('admindashboard') #redirect admin dashboard
         elif user.is_staff:
            return redirect('staffdashboard') #redirect staff dashboard
         else:
            return redirect('studentdashboard') #redirect student dashboard
      else:
         return render(request, 'login.html', {'error': 'Invalid username or password'})
   return render(request, 'login.html')     


def staffregister(request):
      if request.method == 'POST':
         firstname = request.POST.get('firstname')
         lastname = request.POST.get('lastname')
         username = request.POST.get('username')
         password = request.POST.get('password')
         email = request.POST.get('email')
         user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username, email=email, password=password)
         return redirect('members_data')
      else:
         return render(request, 'register.html')

def staff_dashboard(request):
   user=request.user
   context={
      'user':user
   }  
   return render(request,'staffdashboard.html',context)





def dashboard_login(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request,username=username, password=password)
      if user is not None:
         login(request, user)
         return redirect('dashboard')
      else:
         context = {
            'error_message': 'Invalid username or password'
         }

         return render(request, 'login.html',context)
   return render(request, 'login.html')

def userdashboard(request):
   user=request.user
   context={
      'user':user
   }
   return render(request,'dashboard.html',context)


def staffregister(request):
   if request.method=='POST':
      password=request.POST['password']
      email=request.POST['email']
      user=User.object.create_user(username=email,email=email,password=password,is_staff=True)
      return redirect('members_data')
   else:
      return render(request,'staffregister.html')


def studentdashboard(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        user=user.objects.create_user(username=username , email=email ,password=password,is_staff=True)
        return redirect('members_data')
    else:
        return render(request,'studentdashboard.html')


@login_required
def admin_dashboard(request):
   user=request.user

   #Check if the user is a superuser
   if not user.is_superuser:
      return redirect('no_access') # Redirect to an appropriate page
   context={
      'user':user
   }
   return render(request,'admindashboard.html',context)


def user_logout(request):   
   logout(request)
   return redirect('login')

def members(request):
    return HttpResponse("Hello world!")
# Create your views here.

def members_template(request):
 template = loader.get_template('myfirst.html')
 return HttpResponse(template.render())

# def pages_register(request):
#     template=loader.get_template('pr.html')
#     return HttpResponse(request,render())

def pr(request):
    if request.method == 'POST':
         name = request.POST.get('name')
         username = request.POST.get('username')
         password = request.POST.get('password')
         email = request.POST.get('email')
         print("Data received",name,email,username,password)
         user = User.objects.create_user(first_name=name, username=username, email=email, password=password)
         return redirect('members_data')
    else:
       return render(request, 'pr.html')



def Membership_Details(request):
   Employee=EmployeeInfo.objects.all() # fetch all available employees    
   if request.method=='POST':
      club_name=request.POST.get('club_name')
      joining_date=request.POST.get('joining_date')
      Employee_id=request.POST.get('Employee')

      Employee=EmployeeInfo.objects.get(id=Employee_id)
      EmployeeDetails.objects.create(club_name=club_name,joining_date=joining_date,Employee=Employee)
      return redirect('members_data')
   return render(request,'add_employee.html',{'Employee':Employee})

def no_access(request):
   return render(request,'no_access.html')


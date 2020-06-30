from django.shortcuts import render, redirect, resolve_url
from django.contrib import auth, messages
from django.contrib.auth.models import User
from employee.models import  Employee
from jobseeker.models import  Jobseeker
from loggedin.models import LoggedIn
from hr.models import  HR
from django.db import connection
from JokersAdmin.models import Admin
# Create your views here.
def register(request):
    if request.method == 'POST': 
        user_type = request.POST['user_type']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        apartment_no = request.POST['apartment_no']
        street = request.POST['street']
        city = request.POST['city']
        zip_code = request.POST['zip_code']
        age = request.POST['age']
        if (password != password2):
            messages.error(request, 'Password did not match')
            return redirect('register')
        if user_type == 'JobSeeker':
            resume = request.POST['resume']
            jobseekers = Jobseeker.objects.all()
            for jobseeker1 in jobseekers:
                if jobseeker1.username == username:
                    messages.error(request, 'This jobseeker exist in the in the system. Choose another username')
                    return redirect('register')
            jobseeker = Jobseeker()
            jobseeker.username = username
            jobseeker.password = password
            jobseeker.e_mail = email
            jobseeker.name = first_name + ' ' + last_name
            jobseeker.user_type = user_type
            jobseeker.password = password
            jobseeker.password2 = password2
            jobseeker.e_mail = email
            jobseeker.apartment_no = apartment_no
            jobseeker.city = city
            jobseeker.street = street
            jobseeker.zip_code = zip_code
            jobseeker.age = age
            jobseeker.resume = resume
            jobseeker.save()
        if user_type == 'HR':
            company_name = request.POST['company_name']
            hr = HR()
            hr.username = username
            hr.password = password
            hr.e_mail = email
            hr.name = first_name + ' ' + last_name
            hr.user_type = user_type
            hr.apartment_no = apartment_no
            hr.city = city
            hr.street = street
            hr.zip_code = zip_code
            hr.age = age
            hr.company_name = company_name
            hr.save()
        if user_type == 'Employee':
            position = request.POST['position']
            salary = request.POST['salary']
            resume = request.POST['resume']
            employee = Employee()
            employee.username = username
            employee.password = password
            employee.e_mail = email
            employee.name = first_name + ' ' + last_name
            employee.user_type = user_type
            employee.apartment_no = apartment_no
            employee.city = city
            employee.street = street
            employee.zip_code = zip_code
            employee.age = age
            employee.position = position
            employee.salary = salary
            employee.resume = resume
            employee.save()
        messages.success(request, 'Registration Successfull!!')
        return redirect('login')
    else:
        return render(request, 'accounts/register.html')
def logout(request):
    LoggedIn.objects.all().delete()
    return redirect('/')
def login(request):
    if request.method == 'POST':
        user_type = request.POST['user_type']
        print(user_type)
        username = request.POST['username']
        password = request.POST['password']
        if user_type == 'JobSeeker':
            jobseekers = Jobseeker.objects.all()
            for jobseeker1 in jobseekers:
                if jobseeker1.username == username:
                    if jobseeker1.password == password:
                        user_log = LoggedIn()
                        user_log.username = username
                        user_log.password = password
                        user_log.user_type = user_type
                        user_log.save()
                        return redirect('/pages/employee')
            messages.error(request, 'Username did not found, please register.')
            return render(request, 'accounts/register.html')
        if user_type == 'HR':
            hrs = HR.objects.all()
            for hr1 in hrs:
                if hr1.username == username:
                    if hr1.password == password:
                        user_log = LoggedIn()
                        user_log.username = username
                        user_log.password = password
                        user_log.user_type = user_type
                        user_log.save()
                        return redirect('/pages/hr')
            messages.error(request, 'Username did not found, please register.')
            return render(request, 'accounts/register.html')
        if user_type == 'Employee':
            employees = Employee.objects.all()
            for employee1 in employees:
                if employee1.username == username:
                    if employee1.password == password:
                        user_log = LoggedIn()
                        user_log.username = username
                        user_log.password = password
                        user_log.user_type = user_type
                        user_log.save()
                        return redirect('/pages/employee')
            messages.error(request, 'Username did not found, please register.')
            return render(request, 'accounts/register.html')
        if user_type == 'Admin':
            admins = Admin.objects.all()
            for admin1 in admins:
                if admin1.username == username:
                    if admin1.password == password:
                        user_log = LoggedIn()
                        user_log.username = username
                        user_log.password = password
                        user_log.user_type = user_type
                        user_log.save()
                        return redirect('/pages/admin')
            messages.error(request, 'Username did not found, please register.')
            return render(request, 'accounts/register.html')
    else:
        return render(request, 'accounts/login.html')



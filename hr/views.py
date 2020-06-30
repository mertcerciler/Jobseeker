from django.shortcuts import render, redirect, render_to_response
from .models import HR
from django.contrib import auth, messages
from django.db import connection
from user.models import User
from offerings.models import Offerings
from loggedin.models import LoggedIn
from employe_coment.models import Employee_Comment
from employee.models import Employee
from jobseeker.models import Jobseeker
from requested_coment.models import Requested_Coment
import datetime, itertools
from django.core.mail import send_mail

class Counter:
    count1 = 0
    count2 = 0
    def incrementCount1(self):
        self.count1 += 1
        return ''
    def incrementCount2(self):
        self.count2 += 1
        return ''
    def decrement(self):
        self.count1 -= 1
        return ''

    def double(self):
        self.count1 *= 2
        return ''
    def modulo2(self):
        if self.count1 %2 == 0:
            return True
        return False
def hr(request):
    req_coms = Requested_Coment.objects.all()
    hrs = HR.objects.all()
    users = User.objects.all()
    offering = Offerings.objects.all()
    all_comments = Employee_Comment.objects.all()
    counter = Counter()
    context = {
        'counter': counter,
        'req_coms': req_coms,
        'hrs': hrs,
        'users': users,
        'offering': offering,
        'all_comments': all_comments,
    } 
    if request.method == 'POST':
        if request.POST.get('Delete'):
            numb = request.POST['delete']
            print('adsadaas')
            i = 0
            for comment in all_comments:
                if (i == int(numb)):
                    print('adsadaas')
                    id = comment.id
                    instance = Employee_Comment.objects.filter(id=id)
                    instance.delete()
                    messages.success(request, 'Deletion Successful!!')
                    break
                else:
                    i = i + 1    
            return redirect('/pages/admin')
    return render(request, 'pages/CompanyListAdmin.html', context)

def postjob(request):
    all_comments = Employee_Comment.objects.all()
    logged_companies2 = LoggedIn.objects.all()
    hrs2 = HR.objects.all()
    for logged_company in logged_companies2:
        for hr in hrs2:
            if logged_company.username == hr.username:
                edit_password = hr.password
                edit_name = hr.name
                edit_apartmentno = hr.apartment_no
                edit_street = hr.street
                edit_city = hr.city
                edit_companyname = hr.company_name
                edit_email = hr.e_mail
                edit_age = hr.age
                context = {
                    'edit_password': edit_password,
                    'edit_name': edit_name,
                    'edit_apartmentno': edit_apartmentno,
                    'edit_city': edit_city,
                    'edit_street': edit_street,
                    'edit_companyname': edit_companyname,
                    'edit_email': edit_email,
                    'edit_age': edit_age,
                    'i': 0,
                    'all_comments': all_comments,
                }
            else:
                context = {
                    'i': 0,
                    'all_comments': all_comments,
                }
    if request.method == 'POST':
        if request.POST.get("Post"):
            new_offering = Offerings()
            logged_companies = LoggedIn.objects.all()
            hrs = HR.objects.all()
            for logged_company in logged_companies:
                for hr in hrs:
                    if logged_company.username == hr.username:
                        print(logged_company.username)
                        companyname = hr.company_name
                        new_offering.company_name = companyname
                        break
            
            new_offering.name = request.POST['Name']
            new_offering.position = request.POST['Position']
            new_offering.salary = request.POST['Salary']
            new_offering.description = request.POST['Description']
            new_offering.advertising_date = request.POST['Advertising Date']
            new_offering.closing_date = request.POST['Closing Date']
            new_offering.save()
        if request.POST.get("requestbutton"):
            numb = request.POST['request']
            i = 1
            for comment in all_comments:
                if (i == int(numb)):
                    comment.hr_request = True
                    comment.save()
                    break
                else:
                    i = i + 1    
            return redirect('/pages/hr')
        if request.POST.get("Update"):
            new_name = request.POST['Name']
            if new_name:
                for logged_company in logged_companies2:
                    for hr in hrs2:
                        if logged_company.username == hr.username:
                            
                            hr.name = new_name
                            hr.save()
                            break
                return render(request, 'pages/hr.html')
                           
            new_password = request.POST['Password']
            if new_password:
                for logged_company in logged_companies2:
                    for hr in hrs2:
                        if logged_company.username == hr.username:
                            
                            hr.password = new_password
                            hr.save()
                            break
                return render(request, 'pages/hr.html')
                           
            new_apartmentno = request.POST['Apartment_no']
            if new_apartmentno:
                for logged_company in logged_companies2:
                    for hr in hrs2:
                        if logged_company.username == hr.username:
                            
                            hr.apartmentno  = new_apartmentno
                            hr.save()
                            break
                return render(request, 'pages/hr.html')
                           
            new_street = request.POST['Street']
            if new_street:
                for logged_company in logged_companies2:
                    for hr in hrs2:
                        if logged_company.username == hr.username:
                            
                            hr.street = new_street
                            hr.save()
                            break
                return render(request, 'pages/hr.html')
                           
            new_city = request.POST['City']
            if new_city:
                for logged_company in logged_companies2:
                    for hr in hrs2:
                        if logged_company.username == hr.username:
                            
                            hr.city = new_city
                            hr.save()
                            break
                return render(request, 'pages/hr.html')
            new_companyname = request.POST['Company Name']
            if new_companyname:
                for logged_company in logged_companies2:
                    for hr in hrs2:
                        if logged_company.username == hr.username:
                            
                            hr.companyname = new_companyname
                            hr.save()
                            break
                return render(request, 'pages/hr.html')
            new_email = request.POST['E-Mail']
            if new_email:
                for logged_company in logged_companies2:
                    for hr in hrs2:
                        if logged_company.username == hr.username:
                        
                            hr.email = new_email
                            hr.save()
                            break
                return render(request, 'pages/hr.html')
            new_age = request.POST['Age']
            if new_age:
                for logged_company in logged_companies2:
                    for hr in hrs2:
                        if logged_company.username == hr.username:
                            hr.age = new_age
                            hr.save()
                            break
                return render(request, 'pages/hr.html')
                
    return render(request, 'pages/hr.html', context)

def employee(request):
    now = datetime.datetime.now()
    hrs = HR.objects.all()
    employees = Employee.objects.all()
    logged_employees = LoggedIn.objects.all()
    jobseekers = Jobseeker.objects.all()
    all_comments = Employee_Comment.objects.all()
    for logged_employee in logged_employees:
        if logged_employee.user_type == 'Employee':
            for employee1 in employees:
                edit_password = employee1.password
                edit_name = employee1.name
                edit_apartmentno = employee1.apartment_no
                edit_street = employee1.street
                edit_city = employee1.city
                edit_email = employee1.e_mail
                edit_age = employee1.age
                context = {
                    'edit_password': edit_password,
                    'edit_name': edit_name,
                    'edit_apartmentno': edit_apartmentno,
                    'edit_city': edit_city,
                    'edit_street': edit_street,
                    'edit_email': edit_email,
                    'edit_age': edit_age,
                    'hrs': hrs,
                    'logged_employees': logged_employees,
                    'all_comments': all_comments,
                }
            if request.method == 'POST':
                if request.POST.get('Submit'):
                    comment = Employee_Comment()
                    comment.work_experience = request.POST['workexp']
                    comment.interview_process = request.POST['interview']
                    comment.company_pros = request.POST['pros']
                    comment.company_cons = request.POST['cons']
                    comment.comp_name = request.POST['company']
                    employees = Employee.objects.all()
                    anonymous = request.POST.get('anonymous')
                    if not anonymous:
                        comment.ananymous = False
                    for logged_employee in logged_employees:
                        for employee in employees:
                            if logged_employee.username == employee.username:
                                comment.salary_information = employee.salary
                                comment.position = employee.position
                                if not anonymous:
                                    comment.date = employee.username
                                comment.time = str(now.day) + '.' + str(now.month) + '.' + str(now.year) +' ' + str(now.hour) +':' + str(now.minute) +':' + str(now.second)
                                comment.like_dislike_counter = 0
                                comment.hr_request = 'False'
                                comment.save()
                                break
                if request.POST.get('Update'):
                    new_password = request.POST['Password']
                    if new_password:
                        for logged_employee in logged_employees:
                            for employee1 in employees:
                                if logged_employee.username == employee1.username:
                                    employee1.password = new_password
                                    employee1.save()
                                    break
                        return render(request, 'pages/employee.html')
                    new_name = request.POST['Name']
                    if new_name:
                        for logged_employee in logged_employees:
                            for employee1 in employees:
                                if logged_employee.username == employee1.username:
                                    employee1.name = new_name
                                    employee1.save()
                                    break
                        return render(request, 'pages/employee.html')
                    new_apartmentno = request.POST['Apartment_no']
                    if new_apartmentno:
                        for logged_employee in logged_employees:
                            for employee1 in employees:
                                if logged_employee.username == employee1.username:
                                    employee1.apartment_no = new_apartmentno
                                    employee1.save()
                                    break
                        return render(request, 'pages/employee.html')
                    new_street = request.POST['Street']
                    if new_street:
                        for logged_employee in logged_employees:
                            for employee1 in employees:
                                if logged_employee.username == employee1.username:
                                    employee1.street = new_street
                                    employee1.save()
                                    break
                        return render(request, 'pages/employee.html')
                    new_city= request.POST['City']
                    if new_city:
                        for logged_employee in logged_employees:
                            for employee1 in employees:
                                if logged_employee.username == employee1.username:
                                    employee1.city = new_city
                                    employee1.save()
                                    break
                        return render(request, 'pages/employee.html')
                    new_position = request.POST['Position']
                    if new_position:
                        for logged_employee in logged_employees:
                            for employee1 in employees:
                                if logged_employee.username == employee1.username:
                                    employee1.position = new_position
                                    employee1.save()
                                    break
                        return render(request, 'pages/employee.html')
                    new_salary = request.POST['Salary']
                    if new_salary:
                        for logged_employee in logged_employees:
                            for employee1 in employees:
                                if logged_employee.username == employee1.username:
                                    employee1.salary = new_salary
                                    employee1.save()
                                    break
                        return render(request, 'pages/employee.html')
                    new_resume = request.POST['Resume']
                    if new_resume:
                        for logged_employee in logged_employees:
                            for employee1 in employees:
                                if logged_employee.username == employee1.username:
                                    employee1.resume = new_resume
                                    employee1.save()
                                    break
                        return render(request, 'pages/employee.html')
                    new_email = request.POST['E-Mail']
                    if new_email:
                        for logged_employee in logged_employees:
                            for employee1 in employees:
                                if logged_employee.username == employee1.username:
                                    employee1.email = new_email
                                    employee1.save()
                                    break
                        return render(request, 'pages/employee.html')
                    new_age = request.POST['Age']
                    if new_age:
                        for logged_employee in logged_employees:
                            for employee1 in employees:
                                if logged_employee.username == employee1.username:
                                    employee1.age = new_age
                                    employee1.save()
                                    break
                        return render(request, 'pages/employee.html')
        elif logged_employee.user_type == 'JobSeeker':
            for jobseeker1 in jobseekers:
                edit_password = jobseeker1.password
                edit_name = jobseeker1.name
                edit_apartmentno = jobseeker1.apartment_no
                edit_street = jobseeker1.street
                edit_city = jobseeker1.city
                edit_email = jobseeker1.e_mail
                edit_age = jobseeker1.age
                context = {
                    'edit_password': edit_password,
                    'edit_name': edit_name,
                    'edit_apartmentno': edit_apartmentno,
                    'edit_city': edit_city,
                    'edit_street': edit_street,
                    'edit_email': edit_email,
                    'edit_age': edit_age,
                    'hrs': hrs,
                    'logged_employees': logged_employees,
                    'all_comments': all_comments,
                }
            if request.method == 'POST':
                if request.POST.get('Submit'):
                    comment = Employee_Comment()
                    comment.work_experience = request.POST['workexp']
                    comment.interview_process = request.POST['interview']
                    comment.company_pros = request.POST['pros']
                    comment.company_cons = request.POST['cons']
                    comment.comp_name = request.POST['company']
                    
                    anonymous = request.POST.get('anonymous')
                    if not anonymous:
                        comment.ananymous = False
                    for logged_employee in logged_employees:
                        for jobseeker in jobseekers:
                            if logged_employee.username == jobseeker.username:
                                if not anonymous:
                                    comment.date = jobseeker.username
                                comment.time = str(now.day) + '.' + str(now.month) + '.' + str(now.year) +' ' + str(now.hour) +':' + str(now.minute) +':' + str(now.second)
                                comment.like_dislike_counter = 0
                                comment.hr_request = 'False'
                                comment.save()
                                break
                if request.POST.get('Update'):
                    new_password = request.POST['Password']
                    if new_password:
                        for logged_employee in logged_employees:
                            for jobseeker1 in jobseekers:
                                if logged_employee.username == jobseeker1.username:
                                    jobseeker1.password = new_password
                                    jobseeker1.save()
                                    break
                        return render(request, 'pages/employee.html')
                    new_name = request.POST['Name']
                    if new_name:
                        for logged_employee in logged_employees:
                            for jobseeker1 in jobseekers:
                                if logged_employee.username == jobseeker1.username:
                                    jobseeker1.name= new_name
                                    jobseeker1.save()
                                    break
                        return render(request, 'pages/employee.html')
                    new_apartmentno = request.POST['Apartment_no']
                    if new_apartmentno:
                        for logged_employee in logged_employees:
                            for jobseeker1 in jobseekers:
                                if logged_employee.username == jobseeker1.username:
                                    jobseeker1.apartment_no = new_apartmentno
                                    jobseeker1.save()
                                    break
                        return render(request, 'pages/employee.html')
                    new_street = request.POST['Street']
                    if new_street:
                        for logged_employee in logged_employees:
                            for jobseeker1 in jobseekers:
                                if logged_employee.username == jobseeker1.username:
                                    jobseeker1.street = new_street
                                    jobseeker1.save()
                                    break
                        return render(request, 'pages/employee.html')
                    new_city = request.POST['City']
                    if new_city:
                        for logged_employee in logged_employees:
                            for jobseeker1 in jobseekers:
                                if logged_employee.username == employee1.username:
                                    jobseeker1.city = new_city
                                    jobseeker1.save()
                                    break
                        return render(request, 'pages/employee.html')
                    new_resume = request.POST['Resume']
                    if new_resume:
                        for logged_employee in logged_employees:
                            for jobseeker1 in jobseekers:
                                if logged_employee.username == employee1.username:
                                    jobseeker1.resume = new_resume
                                    jobseeker1.save()
                                    break
                        return render(request, 'pages/employee.html')
                    new_email = request.POST['E-Mail']
                    if new_email:
                        for logged_employee in logged_employees:
                            for jobseeker1 in jobseekers:
                                if logged_employee.username == jobseeker1.username:
                                    jobseeker1.e_mail = new_email
                                    jobseeker1.save()
                                    break
                        return render(request, 'pages/employee.html')
                    new_age = request.POST['Age']
                    if new_age:
                        for logged_employee in logged_employees:
                            for jobseeker1 in jobseekers:
                                if logged_employee.username == employee1.username:
                                    jobseeker1.age = new_age
                                    jobseeker1.save()
                                    break
                        return render(request, 'pages/employee.html')

    context = {
        'hrs': hrs,
        'all_comments': all_comments,
        'logged_employees': logged_employees,

    }
    return render(request, 'pages/employee.html', context)
def apply(request):
    print(request.method)
    cursor = connection.cursor()
    hrs = HR.objects.all()
    users = User.objects.all()
    employees = Employee.objects.all()
    logged_employees = LoggedIn.objects.all()
    offering = Offerings.objects.all()
    all_comments = Employee_Comment.objects.all()
    context = {
        'hrs': hrs,
        'users': users,
        'offering': offering,
        'all_comments': all_comments,
    }
    if request.method == 'POST':
        if request.POST.get("applybutton"):
            search = request.POST['search']
            cursor.execute("SELECT * FROM offerings_offerings WHERE company_name LIKE %%s", [search])
            offering = dictfetchall(cursor)
            context = {
                'offering': offering
            }
            return render(request, 'pages/apply2.html', context)
        elif request.POST.get("sortbutton"):
            cursor.execute('SELECT * FROM offerings_offerings  ORDER BY (company_name) DESC;')
            offering = dictfetchall(cursor)
            context = {
                'offering': offering
            }
            return render(request, 'pages/apply2.html', context)
        elif request.POST.get("maxbutton"):
            cursor.execute('SELECT * FROM offerings_offerings GROUP BY id ORDER BY MAX(salary) DESC;')
            offering = dictfetchall(cursor)
            context = {
                'offering': offering
            }
            return render(request, 'pages/apply2.html', context)
        elif request.POST.get("apply"):
           messages.success(request, 'Your application is successfull. Good Luck!!')
    return render(request, 'pages/apply2.html', context)
def dictfetchall(cursor):
    desc = cursor.description
    return[
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

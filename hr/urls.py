from django.urls import path

from . import views

urlpatterns = [
   path('admin', views.hr, name="hr"),
   path('hr', views.postjob, name="postjob"),
   path('employee', views.employee, name="employee"),
   path('apply2', views.apply, name="apply"),
]
 
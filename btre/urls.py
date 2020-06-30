from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('offerings.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('pages/', include('hr.urls')),
]

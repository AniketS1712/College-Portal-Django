"""
URL configuration for academic_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from academy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_views),
    path('Staff_Info/',views.staff_views, name = "Staff"),
    path('staff_template/<str:faculty_name>/',views.staff_temlate_views, name = "stafftemplate"),
    path('Student_Info/',views.student_views, name = "Student"),
    path('Event_Info/',views.event_views, name = "event"),
    path('add_info/',views.add_info, name = "database")
]

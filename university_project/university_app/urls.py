from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('academics/', views.academics, name='academics'),
    path('research/', views.research, name='research'),
    path('campus-life/', views.campus_life, name='campus_life'),
    path('international/', views.international, name='international'),
    path('about/', views.about, name='about'),
    path('controller-of-examinations/', views.controller_of_examinations, name='controller_of_examinations'),
    path('department-finder/', views.department_finder, name='department_finder'),
    path('staff-finder/', views.staff_finder, name='staff_finder'),
    path('program-finder/', views.program_finder, name='program_finder'),
    path('news/', views.news, name='news'),
]

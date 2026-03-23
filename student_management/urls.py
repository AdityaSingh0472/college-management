from django.urls import path
from . import views

urlpatterns = [
    # Student APIs
    path('students/', views.get_students),
    path('students/create/', views.create_student),
    path('students/<int:id>/', views.get_student),
    path('students/update/<int:id>/', views.update_student),
    path('students/delete/<int:id>/', views.delete_student),
    path('students/filter/', views.filter_students),

    # College APIs
    path('colleges/', views.get_colleges),
    path('colleges/create/', views.create_college),
    path('colleges/<int:id>/', views.get_college),
    path('colleges/update/<int:id>/', views.update_college),
    path('colleges/delete/<int:id>/', views.delete_college),
]
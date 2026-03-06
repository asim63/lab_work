from django.urls import path
from . import views

urlpatterns = [
    
    #for question 1
    # path('login/', views.login_view, name='login'),
    # path('dashboard/', views.dashboard_view, name='dashboard'),
    
    ##for question 2
    # path('patient/', views.patient_view, name='patient'),
   
    # #for question 3
    # path('register/', views.register_view, name='register')
    
    # #for question 4
    # path('upload/', views.upload_view, name='upload')
    
    # for question 5
    path('project-submit/', views.project_submit_view, name='project_submit')
]
from django.urls import path
from . import views

urlpatterns = [
    #for question 1
    # path('login/', views.login_view, name='login'),
    # path('dashboard/', views.dashboard_view, name='dashboard'),
    
    ##for question 2
    path('patient/', views.patient_view, name='patient'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('patient/',     views.PatientAPIView.as_view(),      name='patient'),
    path('register/',    views.UserRegAPIView.as_view(),       name='register'),
    path('upload/',      views.ImageUploadAPIView.as_view(),   name='upload'),
    path('project/',     views.ProjectSubmitAPIView.as_view(), name='project'),
    path('notes/',       views.NoteListCreateView.as_view(),   name='notes'),
    path('notes/<int:pk>/', views.NoteDetailView.as_view(),    name='note-detail'),
    path('appointment/', views.AppointmentAPIView.as_view(),   name='appointment'),
    path('login/',       views.StudentLoginAPIView.as_view(),  name='login'),
]
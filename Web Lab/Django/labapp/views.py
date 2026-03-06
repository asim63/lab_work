# #question 1
# from django.shortcuts import render, redirect
# from .models import Student

# def login_view(request):
#     error = ""
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         try:
#             student = Student.objects.get(username=username, password=password)
#             return redirect("dashboard")
#         except Student.DoesNotExist:
#             error = "Invalid username/password"
#     return render(request, "labapp/login.html", {"error": error, "name": "Asim Poudel", "roll": 8})

# def dashboard_view(request):
#     return render(request, "labapp/dashboard.html", {"name": "Asim Poudel", "roll": 8})

from django.shortcuts import render, redirect
from .forms import PatientForm

def patient_view(request):
    form = PatientForm()
    success = False
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    return render(request, "labapp/patient.html", {"form": form, "success": success, "name": "Asim Poudel", "roll": 8})
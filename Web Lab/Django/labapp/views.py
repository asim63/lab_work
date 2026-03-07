#question 1
from django.shortcuts import render, redirect
from .models import Student

def login_view(request):
    error = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            student = Student.objects.get(username=username, password=password)
            return redirect("dashboard")
        except Student.DoesNotExist:
            error = "Invalid username/password"
    return render(request, "labapp/login.html", {"error": error, "name": "Asim Poudel", "roll": 8})

def dashboard_view(request):
    return render(request, "labapp/dashboard.html", {"name": "Asim Poudel", "roll": 8})


# ##for question 2
# from django.shortcuts import render, redirect
# from .forms import PatientForm

# def patient_view(request):
#     form = PatientForm()
#     success = False
#     if request.method == "POST":
#         form = PatientForm(request.POST)
#         if form.is_valid():
#             form.save()
#             success = True
#     return render(request, "labapp/patient.html", {"form": form, "success": success, "name": "Asim Poudel", "roll": 8})

# # for question 3
# from django.shortcuts import render, redirect
# from .forms import UserRegForm
# def register_view(request):
#     form = UserRegForm()
#     success = False
#     if request.method == "POST":
#         form = UserRegForm(request.POST)
#         if form.is_valid():
#             success = True
#             form = UserRegForm()  # reset form
#     return render(request, "labapp/register.html", {
#         "form": form,
#         "success": success,
#         "name": "Asim Poudel",
#         "roll": 8
#     })

# #for question 4
# from django.shortcuts import render
# from .forms import FileUploadForm
# def upload_view(request):
#     form = FileUploadForm()
#     if request.method == "POST":
#         form = FileUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             return render(request, "labapp/upload.html", {"form": form, "success": True, "name": "Asim Poudel", "roll": 8})
#     return render(request, "labapp/upload.html", {"form": form, "name": "Asim Poudel", "roll": 8})

# #for question 5
# from django.shortcuts import render
# from .forms import ProjectSubmitForm
# def project_submit_view(request):
#     form = ProjectSubmitForm()
#     if request.method == "POST":
#         form = ProjectSubmitForm(request.POST, request.FILES)
#         if form.is_valid():
#             return render(request, "labapp/project-submit.html", {"form": form, "success": True, "name": "Asim Poudel", "roll": 8})
#     return render(request, "labapp/project-submit.html", {"form": form, "name": "Asim Poudel", "roll": 8})

#for question 6
from django.shortcuts import render, redirect
from .models import Note
from django.core.exceptions import ValidationError

def note_create(request):
    error = ""
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title and content:
            try:
                note = Note(title=title, content=content)
                note.full_clean()  # ← this triggers validation
                note.save()
                return redirect("note_list")
            except ValidationError as e:
                error = e.messages[0]
        else:
            error = "Both fields are required"
    return render(request, "labapp/note_form.html", {
        "error": error,
        "action": "Create",
        "name": "Asim Poudel",
        "roll": 8
    })
def note_list(request):
    notes = Note.objects.all()
    return render(request, "labapp/notes.html", {"notes": notes, "name": "Asim Poudel", "roll": 8})
def note_edit(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        return redirect('note_list')
    return render(request, "labapp/note_form.html", {"note": note, "name": "Asim Poudel", "roll": 8})

def note_delete(request, pk):
    Note.objects.get(pk=pk).delete()
    return redirect('note_list')

#for question 8
from django.shortcuts import render
from .forms import AppointmentForm

def appointment_view(request):
    form = AppointmentForm()
    success = False
    if request.method == "POST":
        form = AppointmentForm(request.POST, request.FILES)
        if form.is_valid():
            success = True
            form = AppointmentForm()  # reset form
    return render(request, "labapp/appointment.html", {
        "form": form,
        "success": success,
        "name": "Asim Poudel",
        "roll": 8
    })
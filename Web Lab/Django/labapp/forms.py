# from django import forms
# from .models import Patient
# import re

##for question 2
# class PatientForm(forms.ModelForm):
#     class Meta:
#         model = Patient
#         fields = ['name', 'patient_id', 'mobile', 'gender', 'address', 'dob', 'doctor_name']
#         widgets = {
#             'dob': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
#         }

#     def clean_mobile(self):
#         mobile = self.cleaned_data.get('mobile')
#         if not re.match(r'^(98|97|96)\d{8}$', mobile):
#             raise forms.ValidationError("Mobile must be 10 digits starting with 98, 97, or 96")
#         return mobile

# #for question 3 
# import re

# class UserRegForm(forms.Form):
#     full_name = forms.CharField(max_length=40)
#     email = forms.EmailField()
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)

#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         if not re.match(r'^[a-zA-Z]+\d+$', username):
#             raise forms.ValidationError("Username must start with letters followed by numbers")
#         return username

#     def clean_password(self):
#         password = self.cleaned_data.get('password')
#         if len(password) <= 8:
#             raise forms.ValidationError("Password must be more than 8 characters")
#         return password

# #for question 4
# class FileUploadForm(forms.Form):
#     file = forms.FileField()

#     def clean_file(self):
#         file = self.cleaned_data.get('file')
#         if file:
#             ext = file.name.split('.')[-1].lower()
#             if ext not in ['jpg', 'jpeg', 'png', 'gif']:
#                 raise forms.ValidationError("Only jpg, jpeg, png, gif allowed")
#             if file.size > 2 * 1024 * 1024:
#                 raise forms.ValidationError("File size must be less than 2MB")
#         return file


# #for question 5
# from django import forms
# class ProjectSubmitForm(forms.Form):
#     tu_reg = forms.CharField(label="TU Registration Number")
#     email = forms.EmailField()
#     project_file = forms.FileField()

#     def clean_project_file(self):
#         file = self.cleaned_data.get('project_file')
#         if file:
#             ext = file.name.split('.')[-1].lower()
#             allowed = ['pdf', 'doc', 'docx', 'ppt', 'pptx', 'jpeg']
#             if ext not in allowed:
#                 raise forms.ValidationError(f"Allowed formats: {', '.join(allowed)}")
#             if file.size > 5 * 1024 * 1024:
#                 raise forms.ValidationError("File must be less than 5MB")
#         return file


#for question 8
from datetime import date
import re
from django import forms

class AppointmentForm(forms.Form):
    name = forms.CharField(label="Full Name")
    gender = forms.ChoiceField(choices=[
        ('', 'Select Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ])
    hobbies = forms.CharField(label="Hobbies")
    appointment = forms.DateTimeField(
        label="Appointment Date & Time",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )
    country = forms.CharField(label="Country")
    resume = forms.FileField(label="Resume")
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Phone Number")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean_appointment(self):
        appt = self.cleaned_data.get('appointment')
        if appt and appt.date() < date.today():
            raise forms.ValidationError("Appointment date cannot be in the past")
        return appt

    def clean_resume(self):
        file = self.cleaned_data.get('resume')
        if file:
            ext = file.name.split('.')[-1].lower()
            allowed = ['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png']
            if ext not in allowed:
                raise forms.ValidationError("Resume must be pdf, doc, docx, jpg, jpeg or png")
            if file.size > 2 * 1024 * 1024:
                raise forms.ValidationError("Resume must be less than 2MB")
        return file

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^(9\d{9}|01\d{7})$', phone):
            raise forms.ValidationError("Phone must be 9XXXXXXXXX or 01XXXXXXX")
        return phone

    def clean_password(self):
        pw = self.cleaned_data.get('password')
        if len(pw) < 8:
            raise forms.ValidationError("Password must be at least 8 characters")
        if not re.search(r'[a-z]', pw):
            raise forms.ValidationError("Password must contain at least one lowercase letter")
        if not re.search(r'[A-Z]', pw):
            raise forms.ValidationError("Password must contain at least one uppercase letter")
        if not re.search(r'\d', pw):
            raise forms.ValidationError("Password must contain at least one number")
        if not re.search(r'[!@#$%^&*()_+\-=\[\]{}]', pw):
            raise forms.ValidationError("Password must contain at least one symbol")
        return pw

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Password and confirm password do not match")
        return cleaned_data
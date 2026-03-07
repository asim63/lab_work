from rest_framework import serializers
from .models import Patient, Note
from datetime import date
import re


# Program 3 - Patient
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Patient
        fields = ['id', 'name', 'patient_id', 'mobile',
                  'gender', 'address', 'dob', 'doctor_name']

    def validate_mobile(self, value):
        if not re.match(r'^(98|97|96)\d{8}$', value):
            raise serializers.ValidationError(
                "Mobile must be 10 digits starting with 98, 97, or 96")
        return value


# Program 4 - User Registration
class UserRegSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=40)
    email     = serializers.EmailField()
    username  = serializers.CharField()
    password  = serializers.CharField(write_only=True)

    def validate_username(self, value):
        if not re.match(r'^[a-zA-Z]+\d+$', value):
            raise serializers.ValidationError(
                "Username must start with letters followed by numbers")
        return value

    def validate_password(self, value):
        if len(value) <= 8:
            raise serializers.ValidationError(
                "Password must be more than 8 characters")
        return value


# Program 5 - Image Upload
class ImageUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    def validate_file(self, value):
        ext = value.name.split('.')[-1].lower()
        if ext not in ['jpg', 'jpeg', 'png', 'gif']:
            raise serializers.ValidationError(
                "Only jpg, jpeg, png, gif files are allowed")
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                "File size must be less than 2MB")
        return value


# Program 6 - Project Submission
class ProjectSubmitSerializer(serializers.Serializer):
    tu_reg       = serializers.CharField(label="TU Registration Number")
    email        = serializers.EmailField()
    project_file = serializers.FileField()

    def validate_project_file(self, value):
        ext     = value.name.split('.')[-1].lower()
        allowed = ['pdf', 'doc', 'docx', 'ppt', 'pptx', 'jpeg']
        if ext not in allowed:
            raise serializers.ValidationError(
                f"Allowed formats: {', '.join(allowed)}")
        if value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError(
                "File must be less than 5MB")
        return value


# Program 7 - Notes CRUD
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Note
        fields = ['id', 'title', 'content', 'created_at']


# Program 8 - Appointment
class AppointmentSerializer(serializers.Serializer):
    name             = serializers.CharField()
    gender           = serializers.ChoiceField(
                           choices=['Male', 'Female', 'Other'])
    hobbies          = serializers.CharField()
    appointment      = serializers.DateTimeField()
    country          = serializers.CharField()
    resume           = serializers.FileField()
    email            = serializers.EmailField()
    phone            = serializers.CharField()
    password         = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate_appointment(self, value):
        if value.date() < date.today():
            raise serializers.ValidationError(
                "Appointment date cannot be in the past")
        return value

    def validate_resume(self, value):
        ext = value.name.split('.')[-1].lower()
        if ext not in ['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png']:
            raise serializers.ValidationError(
                "Resume must be pdf, doc, docx, or image")
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                "Resume must be less than 2MB")
        return value

    def validate_phone(self, value):
        if not re.match(r'^(9\d{9}|01\d{7})$', value):
            raise serializers.ValidationError(
                "Phone must be 9XXXXXXXXX or 01XXXXXXX")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters")
        if not re.search(r'[a-z]', value):
            raise serializers.ValidationError(
                "Password needs a lowercase letter")
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError(
                "Password needs an uppercase letter")
        if not re.search(r'\d', value):
            raise serializers.ValidationError(
                "Password needs a number")
        if not re.search(r'[!@#$%^&*()_+\-=\[\]{}]', value):
            raise serializers.ValidationError(
                "Password needs a symbol")
        return value

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError(
                "Password and confirm password do not match")
        return data
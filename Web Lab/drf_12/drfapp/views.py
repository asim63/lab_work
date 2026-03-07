from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Student, Note
from .serializers import (
    PatientSerializer, UserRegSerializer, ImageUploadSerializer,
    ProjectSubmitSerializer, NoteSerializer, AppointmentSerializer
)

STUDENT_TAG = "Asim Poudel | Roll: 8"


# Program 3 - Patient
class PatientAPIView(APIView):
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": f"Patient saved - {STUDENT_TAG}",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Program 4 - User Registration
class UserRegAPIView(APIView):
    def post(self, request):
        serializer = UserRegSerializer(data=request.data)
        if serializer.is_valid():
            return Response({
                "message": f"User registered - {STUDENT_TAG}",
                "data": serializer.validated_data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Program 5 - Image Upload
class ImageUploadAPIView(APIView):
    def post(self, request):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            return Response({
                "message": f"Image uploaded - {STUDENT_TAG}",
                "filename": request.FILES['file'].name
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Program 6 - Project Submission
class ProjectSubmitAPIView(APIView):
    def post(self, request):
        serializer = ProjectSubmitSerializer(data=request.data)
        if serializer.is_valid():
            return Response({
                "message": f"Project submitted - {STUDENT_TAG}",
                "tu_reg": serializer.validated_data['tu_reg'],
                "email":  serializer.validated_data['email']
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Program 7 - Notes CRUD
class NoteListCreateView(APIView):
    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response({
            "student": STUDENT_TAG,
            "notes": serializer.data
        })

    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetailView(APIView):
    def get_object(self, pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            return None

    def get(self, request, pk):
        note = self.get_object(pk)
        if not note:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(NoteSerializer(note).data)

    def put(self, request, pk):
        note = self.get_object(pk)
        if not note:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        note = self.get_object(pk)
        if not note:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        note.delete()
        return Response({"message": "Note deleted"}, status=status.HTTP_204_NO_CONTENT)


# Program 8 - Appointment
class AppointmentAPIView(APIView):
    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            return Response({
                "message": f"Appointment registered - {STUDENT_TAG}",
                "name":  serializer.validated_data['name'],
                "email": serializer.validated_data['email']
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Program 9 - JWT Login
class StudentLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            student = Student.objects.get(
                username=username, password=password)
            refresh = RefreshToken()
            refresh['username'] = student.username
            return Response({
                "message":  f"Login successful - {STUDENT_TAG}",
                "username": student.username,
                "refresh":  str(refresh),
                "access":   str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response(
                {"error": "Invalid username/password"},
                status=status.HTTP_401_UNAUTHORIZED)
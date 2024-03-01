from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Doctor,Specialization,Designation,AvailableTime,Review
from .serializers import DoctorSerializer,SpecializationSerializer,DesignationSerializer,AvailableTimeSerializer,ReviewSerializer
from rest_framework.permissions import IsAuthenticated,BasePermission,IsAuthenticatedOrReadOnly
from rest_framework import filters,pagination

class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    
class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
 
class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
       doctor_id = request.query_params.get("doctor_id")
       if doctor_id:
           return queryset.filter(doctor = doctor_id)
       return queryset
       
class AvailableTimeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
    filter_backends= [AvailableTimeForSpecificDoctor]

class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1 
    page_size_query_param = page_size
    max_page_size = 100 
    
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    pagination_class = DoctorPagination
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name', 'user__email', 'designation__name', 'specialization__name']

class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
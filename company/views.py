from django.shortcuts import render
from rest_framework import generics
from .models import CompanyInfo, Project, Leadership, JobOpening, MissionVision
from .serializers import CompanyInforSerializer, ProjectSerializer, LeadershipSerializer, JobOpeningSerializer, MissionVisionSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
# Create your views here.

# Cache thoi gian la 1 ngay
CACHE_TTL = 60*60*24

@method_decorator(cache_page(CACHE_TTL),name='get') # Cache chỉ cho phương thức GET
class CompanyInforView(generics.RetrieveAPIView):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInforSerializer

    


class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectSerializer
     
    
    # sử dụng get_queryset vì ở đây, cần truy vấn động - dựa trên company_id
    def get_queryset(self):
        company_id=self.kwargs['company_id']
        return Project.objects.filter(company_id=company_id).select_related('company')
    

class LeadershipListView(generics.ListAPIView):
    serializer_class= LeadershipSerializer

    def get_queryset(self):
        company_id = self.kwargs['company_id']

        return Leadership.objects.filter(company_id=company_id).select_related('company')

class JobOpeningListView(generics.ListAPIView):
    serializer_class = JobOpeningSerializer

    def get_queryset(self):
        company_id = self.kwargs['company_id']
        return JobOpening.objects.filter(company_id=company_id).select_related('company')


@method_decorator(cache_page(CACHE_TTL), name='get') 
class MissionVisionView(generics.RetrieveAPIView):
    serializer_class = MissionVisionSerializer

    def get_queryset(self):
        company_id = self.kwargs['company_id']

        return MissionVision.objects.filter(company_id=company_id)

    

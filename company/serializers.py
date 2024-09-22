from rest_framework import serializers
from .models import CompanyInfo,Project,Leadership,JobOpening,MissionVision


class CompanyInforSerializer(serializers.ModelSerializer):
    class Meta:
        model=CompanyInfo
        fields=['name', 'founding_date', 'ceo', 'father_company', 'amount_staff', 'address', 'description', 'logo']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=['title', 'description', 'start_date', 'end_date', 'client', 'technologies_used', 'project_link']

class MissionVisionSerializer(serializers.ModelSerializer):
     class Meta:
        model = MissionVision
        fields = ['mission', 'vision']


class JobOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOpening
        fields=['title', 'description', 'requirements', 'posted_date', 'application_deadline', 'job_type']

class LeadershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leadership
        fields = ['name', 'position', 'bio', 'photo', 'linkedin_profile']
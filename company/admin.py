from django.contrib import admin
from .models import CompanyInfo,Project,Leadership,JobOpening,MissionVision

# Register your models here.
admin.site.register(CompanyInfo)
admin.site.register(Project)
admin.site.register(Leadership)
admin.site.register(JobOpening)
admin.site.register(MissionVision)

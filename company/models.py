from django.db import models


class CompanyInfo(models.Model):
    name = models.CharField(max_length=255)
    founding_date = models.CharField(max_length=50)
    ceo = models.CharField(max_length=50)
    father_company = models.CharField(max_length=255)
    amount_staff = models.CharField(max_length=255)
    address = models.TextField()  
    description = models.TextField()  
    logo = models.ImageField(upload_to='company_logo/', null=True, blank=True)  
    

    class Meta: 
        db_table='company'
    def __str__(self):
        return self.name


class Project(models.Model):
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE, related_name='projects') 
    title = models.CharField(max_length=255)  
    description = models.TextField() 
    start_date = models.DateField() 
    end_date = models.DateField(null=True, blank=True)  
    client = models.CharField(max_length=255)  
    technologies_used = models.CharField(max_length=255)  
    project_link = models.URLField(null=True, blank=True)


    class Meta:
        db_table = 'company_project'  

    def __str__(self):
        return self.title



class Leadership(models.Model):
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE, related_name='leadership')
    name = models.CharField(max_length=255)  
    position = models.CharField(max_length=255)  
    bio = models.TextField() 
    photo = models.ImageField(upload_to='leadership_photos/', null=True, blank=True)  
    linkedin_profile = models.URLField(null=True, blank=True)

    class Meta:
        db_table='company_leadership' 

    def __str__(self):
        return f"{self.name} - {self.position}"



class JobOpening(models.Model):
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE, related_name='job_openings') 
    title = models.CharField(max_length=255)  
    description = models.TextField()  
    requirements = models.TextField()
    posted_date = models.DateField(auto_now_add=True)  
    application_deadline = models.DateField()  
    job_type = models.CharField(max_length=50, choices=[('FT', 'Full-time'), ('PT', 'Part-time'), ('CT', 'Contract')])  


    class Meta:
        db_table='job_opening'

    def __str__(self):
        return self.title



class MissionVision(models.Model):
    company = models.OneToOneField(CompanyInfo, on_delete=models.CASCADE, related_name='mission_vision') 
    mission = models.TextField() 
    vision = models.TextField()  


    class Meta:
        db_table='company_mission'

    def __str__(self):
        return "Mission and Vision"

from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verifird = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)
    
class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
   
    
    
class Company(models.Model):
    user_id = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    companyname = models.CharField(max_length=150)
    website = models.CharField(max_length=255)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    email = models.CharField(max_length=150)

        
class JobPost(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    experience = models.DecimalField(max_digits=10, decimal_places=1)  # In years
    website = models.URLField(max_length=255)
    logo = models.ImageField(upload_to='logos/')
    posted_on = models.DateTimeField(auto_now_add=True)        
    
class JobApplication(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    cover_letter = models.TextField()
    job_position = models.CharField(max_length=200)
    resume = models.FileField(upload_to='resumes/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)  # Optional user field


       
    
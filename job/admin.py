from django.contrib import admin
from .models import UserMaster, Candidate, Company, JobPost, JobApplication

# Register your models here.

admin.site.register(UserMaster)
admin.site.register(Candidate)
admin.site.register(Company)
admin.site.register(JobPost)
admin.site.register(JobApplication)

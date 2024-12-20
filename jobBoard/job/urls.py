from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
  path("",views.HomePage,name="home") ,
  path("index/",views.IndexPage,name="index") ,
  path("company/",views.CompanyPage,name="company") ,
  path("signup/",views.SignupPage,name="signup"),
  path("register/",views.RegisterUser,name="register"),
  path("loginpage/",views.LoginPage,name="loginpage"),
  path("loginuser/",views.loginUser,name="login"),
  path("canpro/<int:pk>/",views.Canpro,name="canpro"),
  path("comnpro/<int:pk>/",views.Comnpro,name="comnpro"),
  path("logout/",views.logOut,name="logout"),
  path("updatecan/<int:pk>/",views.UpdateCan,name="updatecan"),
  path("updatecom/<int:pk>/",views.UpdateCom,name="updatecom"),
  path("post_job/<int:pk>/", views.post_job, name='post_job'),
  path("job_post_submit/<int:pk>/", views.post_job_submit, name='jobsubmit'),
  path("show_job_date/<int:pk>/", views.show_job_date, name='jobdata'),
  path("job_update/<int:id>/", views.job_update, name='jobupdate'),
  path("job_updated/<int:id>/", views.job_updated, name='jobupdated'),
  path("job_delete/<int:id>/<int:pk>/", views.Delete_job, name='jobdeleted'), 
  path("joblist/", views.job_list_candidate, name="joblist"),
  path("job_details/<int:id>/", views.job_Details, name="job_details"),
  path("job_application/<int:id>/<int:num>/", views.job_Application, name="job_application"),
  path("job_apply/<int:id>/<int:num>/", views.job_Apply, name="job_apply"),
  path("job_applicants/<int:id>/", views.job_applicants, name="job_applicants"),
  path("application_delete/<int:id>/", views.application_delete, name="application_delete"),
]
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.contrib import messages
from django.db.models import Count, Avg, Sum
from random import randint
from .models import UserMaster, Candidate, Company, JobPost, JobApplication
from django.utils import timezone

# Create your views here.

def HomePage(request):
    return render(request, "app/home.html")

def IndexPage(request):
    return render(request, "app/index.html")

def CompanyPage(request):
    return render(request, "app/company/index.html")

def SignupPage(request):
    return render(request, "app/signup.html")

def RegisterUser(request):
    try:
        role = request.POST['role']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        user = UserMaster.objects.filter(email=email)
        if user:
            message = "User already exists"
            return render(request, "app/signup.html", {'msg': message})

        if password == confirm_password:
            otp = randint(10000, 999999)
            newuser = UserMaster.objects.create(role=role, otp=otp, email=email, password=password)

            if role == "Candidate":
                Candidate.objects.create(user_id=newuser, firstname=fname, lastname=lname)
            elif role == "Company":
                Company.objects.create(user_id=newuser, firstname=fname, lastname=lname)

            return render(request, "app/login.html")
        else:
            message = "Passwords do not match"
            return render(request, "app/signup.html", {'msg': message})
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect("signup")

def LoginPage(request):
    return render(request, "app/login.html")

def loginUser(request):
    try:
        if request.method == "POST":
            role = request.POST.get("role")
            email = request.POST.get("email")
            password = request.POST.get("password")

            user = UserMaster.objects.get(email=email)

            if role.lower() == "candidate" and user.role.lower() == "candidate":
                if user.password == password:
                    can = Candidate.objects.get(user_id=user)
                    request.session["id"] = user.id
                    request.session["role"] = user.role
                    request.session["firstname"] = can.firstname
                    request.session["lastname"] = can.lastname
                    request.session["email"] = user.email
                    request.session["password"] = user.password
                    return redirect("index")
                else:
                    msg = "Password does not match"
                    return render(request, "app/login.html", {"msg": msg})

            elif role.lower() == "company" and user.role.lower() == "company":
                if user.password == password:
                    comp = Company.objects.get(user_id=user)
                    request.session["id"] = user.id
                    request.session["role"] = user.role
                    request.session["firstname"] = comp.firstname
                    request.session["lastname"] = comp.lastname
                    request.session["email"] = user.email
                    request.session["password"] = user.password
                    return redirect("company")
                else:
                    msg = "Password does not match"
                    return render(request, "app/login.html", {"msg": msg})

            else:
                msg = "Invalid role selected"
                return render(request, "app/login.html", {"msg": msg})

    except UserMaster.DoesNotExist:
        msg = "User does not exist"
        return render(request, "app/login.html", {"msg": msg})
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return render(request, "app/login.html")

def Canpro(request, pk):
    try:
        user = UserMaster.objects.get(pk=pk)
        can = Candidate.objects.get(user_id=user)
        return render(request, "app/canpro.html", {'user': user, 'can': can})
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect("index")

def UpdateCan(request, pk):
    try:
        user = UserMaster.objects.get(pk=pk)
        if user.role == "Candidate":
            can = Candidate.objects.get(user_id=user)
            can.state = request.POST.get('state')
            can.city = request.POST.get('city')
            can.education = request.POST.get('education')
            can.website = request.POST.get('website')
            can.contact = request.POST.get('contact')
            can.gender = request.POST.get('gender')
            can.address = request.POST.get('address')
            can.firstname = request.POST.get('firstname')
            can.lastname = request.POST.get('lastname')
            can.dob = request.POST.get('dob')
            can.save()
            url = f'/canpro/{pk}'
            return redirect(url)
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect("index")

def Comnpro(request, pk):
    try:
        user = UserMaster.objects.get(pk=pk)
        com = Company.objects.get(user_id=user)
        return render(request, "app/company/comnpro.html", {'user': user, 'com': com})
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect("index")

def UpdateCom(request, pk):
    try:
        user = UserMaster.objects.get(pk=pk)
        if user.role == "Company":
            com = Company.objects.get(user_id=user)
            com.firstname = request.POST.get('firstname')
            com.lastname = request.POST.get('lastname')
            com.companyname = request.POST.get('company')
            com.website = request.POST.get('website')
            com.address = request.POST.get('address')
            com.contact = request.POST.get('contact')
            com.email = request.POST.get('email')
            com.state = request.POST.get('state')
            com.city = request.POST.get('city')
            com.save()
            url = f'/comnpro/{pk}'
            return redirect(url)
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect("index")

def post_job(request, pk):
    return render(request, "app/company/jobpost.html")

def post_job_submit(request, pk):
    try:
        user = UserMaster.objects.get(id=pk)
        if user.role == "Company":
            comp = Company.objects.get(user_id=user)
            name = request.POST['name']
            title = request.POST['title']
            description = request.POST['description']
            salary = request.POST['salary']
            experience = request.POST['experience']
            website = request.POST['website']
            logo = request.FILES['logo']

            JobPost.objects.create(company_id=comp, title=title, description=description, salary=salary, \
                                   experience=experience, website=website, logo=logo, name=name)

            msg = "Job posted successfully"
            return render(request, "app/company/jobpost.html", {'msg': msg})
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect("index")

def show_job_date(request, pk):
    try:
        user = UserMaster.objects.get(id=pk)
        com = Company.objects.get(user_id_id=user)
        company = com.id
        job_posts = JobPost.objects.all()
        return render(request, 'app/company/job_posted.html', {'job_posts': job_posts, "company_id": company})
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect("index")

def job_update(request, id):
    try:
        job = JobPost.objects.get(id=id)
        return render(request, "app/company/edit_job.html", {"job": job})
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect("index")

def job_updated(request, id):
    try:
        if request.method == "POST":
            job = get_object_or_404(JobPost, id=id)
            job.name = request.POST.get('name', job.name)
            job.title = request.POST.get('title', job.title)
            job.description = request.POST.get('description', job.description)
            job.salary = request.POST.get('salary', job.salary)
            job.experience = request.POST.get('experience', job.experience)
            job.website = request.POST.get('website', job.website)
            if request.FILES.get('logo'):
                job.logo = request.FILES['logo']
            job.save()
            messages.success(request, "Job details updated successfully!")
            return redirect(reverse('jobupdate', args=[id]))
        return redirect(reverse('jobupdate', args=[id]))
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect("index")

def Delete_job(request, id, pk):
    try:
        job = get_object_or_404(JobPost, id=id)
        job.delete()
        messages.success(request, "Job deleted successfully!")
        return redirect('jobdata', pk=pk)
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect("index")

def job_list_candidate(request):
    try:
        jobs = JobPost.objects.all()
        return render(request, "app/job-list.html", {"jobs": jobs})
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect("index")

def job_Details(request, id):
    try:
        job = JobPost.objects.get(id=id)
        return render(request, "app/job-details.html", {"job": job})
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect("index")

def job_Application(request, id, num):
    try:
        return render(request, "app/job-application.html", {"id": id, "num": num})
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect("index")


def job_Apply(request, id, num):
    try:
        job_post = get_object_or_404(JobPost, id=id)
        company = Company.objects.get(id=num)

        if request.method == "POST":
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            cover_letter = request.POST.get('cover_letter')
            resume = request.FILES.get('resume')
            job_position = request.POST.get('job_position')

            # Get the logged-in user (optional)
            user = request.user if request.user.is_authenticated else None

            JobApplication.objects.create(
                company=company,
                job_post=job_post,
                firstname=firstname,
                lastname=lastname,
                email=email,
                phone=phone,
                address=address,
                cover_letter=cover_letter,
                resume=resume,
                job_position=job_position,
                user=user  # Add the user field
            )
            msg = "Your job application has been submitted successfully!"
            return redirect(f'/job_details/{id}/?msg={msg}')

        return render(request, "app/job-application.html", {'job_post': job_post, 'id': id, 'num': num })
    except Exception as e:
        return render(request, "app/job-application.html", {'error': str(e), 'id': id, 'num': num })

def job_applicants(request, id):
    try:
        job_applications = JobApplication.objects.filter(company_id=id)
        return render(request, "app/company/job_applicants.html", {"job_applications": job_applications})
    except Exception as e:
        return render(request, "app/company/job_applicants.html", {"error": str(e)})

def application_delete(request, id):
    try:
        job = get_object_or_404(JobApplication, id=id)
        job.delete()
        messages.success(request, "Applicant deleted successfully!")
        return redirect('job_applicants', id=id)
    except Exception as e:
        messages.error(request, f"Error deleting applicant: {str(e)}")
        return redirect('job_applicants', id=id)

def logOut(request):
    try:
        del request.session["email"]
        del request.session["password"]
    except KeyError:
        pass
    return redirect("home")

 
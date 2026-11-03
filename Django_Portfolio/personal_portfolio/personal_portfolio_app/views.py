from django.shortcuts import render
from .models import (
    Profile,
    About,
    Education,
    Skill,
    CareerGoal,
    Project,
    Contact,
)

# Create your views here.
from django.http import HttpResponse

def home(request):
    profile = Profile.objects.first()
    about = About.objects.first()
    educations = Education.objects.order_by('-end_year', '-start_year')
    skills = Skill.objects.all().order_by('-id')
    career_goal = CareerGoal.objects.first()
    latest_projects = Project.objects.order_by('-created_at')[:3]

    context = {
        'profile': profile,
        'about': about,
        'educations': educations,
        'skills': skills,
        'career_goal': career_goal,
        'latest_projects': latest_projects,
    }

    return render(request, 'personal_portfolio_app/home.html', context)


def projects(request):
    projects = Project.objects.order_by('-created_at')

    context = {
        'projects': projects,
    }

    return render(request, 'personal_portfolio_app/projects.html', context)


def contact(request):
    success = False
    error = False
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        
        if name and email and message:
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            success = True
        else:
            error = True
    
    return render(request, 'personal_portfolio_app/contact.html', {
        'success': success,
        'error': error
    })
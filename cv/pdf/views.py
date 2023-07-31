from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

# Create your views here.
def accept(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone_number = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        education = request.POST.get("education","")
        
        work_experience= request.POST.get("work_experience","")
        projects = request.POST.get("projects","")
        skills = request.POST.get("skills","")
        profile = Profile(name=name,email=email,phone_number=phone_number,summary=summary,education=education,work_experience=work_experience,projects=projects,skills=skills)
        profile.save()
    

    return render(request, 'pdf/accept.html')
def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile':user_profile})
    options ={
    'page-size':'Letter',
    'encoding':"UTF-8",
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] ='attachment'
    filename = "resume.pdf"
    return response

def list(request):
    profiles = Profile.objects.all()
    return render(request,'pdf/list.html',{'profiles':profiles})
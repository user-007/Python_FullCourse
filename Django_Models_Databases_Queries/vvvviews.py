from django.shortcuts import render
from .models import Profile



def accept(request):
    if request.method = "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        summary = request.POST.get("summary", "")
        degree = request.POST.get("degree", "")
        school = request.POST.get("school", "")
        university = request.POST.get("university","")
        previous_role = request.POST.get("previous_file","")
        skills = request.POST.get("skills", "")

        profile = Profile(name=name, email=email, phone=phone,summary=summary)
        profile.save()
def resume(request, id):
    user_profile = Profile.object.get(pk=id)
    return render(request, 'pdf/resume.html', {})
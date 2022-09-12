from django.shortcuts import render

def resume_page(request):
    return render(request, 'resume.html')

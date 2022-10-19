from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .contact_form import ContactForm

# Create your views here.


def portfolio(request):
    return render(request, 'Portfolio/index.html', {'title': 'Portfolio'})


def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            your_name = form.cleaned_data["your_name"]
            your_email = form.cleaned_data["your_email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data['message']
            try:
                send_mail(your_name, your_email, subject,
                          message, ["admin@example.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "Portfolio/success.html", {"form": form})


def successView(request):
    return render(request, "Portfolio/success.html")
    # return HttpResponse("Success! Thank you for your message.")

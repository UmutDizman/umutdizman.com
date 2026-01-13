from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.translation import gettext as _
import threading
from .tasks import send_inquiry_emails
from .forms import InquiryForm
import logging
# Create your views here.

logger = logging.getLogger(__name__)

def home(request):
    return render(request, "index.html")

def services(request):
    return render(request, "services.html")

def projects(request):
    return render(request, "projects.html")

def about(request):
    return render(request, "about.html")

def hire_me(request):
    return render(request, "hire_me.html")


def contact_view(request):
    preset = (request.GET.get("package") or "").strip().lower()  # /contact?package=starter

    if request.method == "POST":
        form = InquiryForm(request.POST, preset_package=preset)
        if form.is_valid():
            inquiry = form.save(commit=False)

            if preset in {"starter", "business", "pro"}:
                inquiry.package = preset  # garanti

            inquiry.save()

            threading.Thread(
                target=send_inquiry_emails,
                args=(inquiry,),
                daemon=True
            ).start()
            

            messages.success(request, _("Thanks! Your message has been sent."))
            return redirect("umutdizmancom:contact_success")

    else:
        form = InquiryForm(preset_package=preset)

    return render(request, "contact.html", {"form": form, "preset_package": preset})


def contact_success_view(request):
    return render(request, "contact_success.html")
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('name', '')
            content = request.POST.get('name', '')
            #Enviamos correo
            email =EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["victorm.brioness@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                #todo ha ido bien
                return redirect(reverse("contact")+"?fail")
            except:
                #algo no ha ido bien..
                return redirect(reverse('contact')+"?Fail")

    return render(request, "contact/contact.html",{'form':contact_form})

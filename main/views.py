from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django import forms
from django.shortcuts import reverse, redirect, render
from django.views.generic import TemplateView, FormView


# Create your views here.

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your name'}))

    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Your email'})
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your message'})
    )

class SuccessView(TemplateView):
    template_name = 'success.html'

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

        full_message = f"""
            Received message below from {name}, {email}
            ___________________
            
            
            {message}
        """

        send_mail(
            subject = "Received contact form submission",
            message = full_message,
            from_email = settings.DEFAULT_FROM_EMAIL,
            recipient_list = [settings.NOTIFY_EMAIL],
        )
        return super(ContactView, self).form_valid(form)

def home(request):
    return render(request, 'home.html', None)

def portfolio(request):
    target_url = 'https://github.com/WillRunIt'
    return redirect(target_url)

def about(request):
    return render(request, 'about.html', None)

def experience(request):
    return render(request, 'experience.html', None)

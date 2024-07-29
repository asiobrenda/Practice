from django.shortcuts import render, redirect, reverse
#from django.http import HttpResponse
from .forms import SignUpCreationForm
from .models import (Home, Biography, Skills, Services, Portfolio, Testimonial, Contact)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db import connection
from django.apps import apps
from django.http import JsonResponse
import threading
from django.core.mail import send_mail
from django.core.mail import EmailMessage
#from .utils import send_email_async

def index(request, category=None):
    skills = Skills.objects.all()
    #print(skills)
    bio = Biography.objects.all()
    home = Home.objects.all()
    service = Services.objects.all()
    testimonial = Testimonial.objects.all()

    #if statement for portfolio
    if category:
        portfolio = Portfolio.objects.filter(category=category)
    else:
        portfolio = Portfolio.objects.all()
    return render(request, 'brenda/home.html', {'home':home, 'skills':skills, 'bio':bio,
                                                'service':service, 'portfolio': portfolio,
                                                'testimonial':testimonial})


def send_email_async(subject, message, from_email, to_email):
    email = EmailMessage(
        subject,
        message,
        from_email,
        [to_email],
        headers={'Reply-To': from_email}
    )
    threading.Thread(target=email.send).start()

def contact(request):
    if request.method == "POST":
        contact_name = request.POST.get('name')
        contact_email = request.POST.get('email')
        contact_subject = request.POST.get('subject')
        contact_message = request.POST.get('message')

        if contact_subject == '' or contact_message == '':
            return_message = {'status': 'ko', 'message': 'Must enter subject and a message!'}
        else:
            details = Contact.objects.create(
                name=contact_name,
                email=contact_email,
                subject=contact_subject,
                message=contact_message,
            )
            # Send email in a separate thread
            send_email_async(contact_subject, contact_message, contact_email, 'asiobrenda01@gmail.com')

            return_message = {'status': 'ok', 'message': 'Data received successfully'}
        return JsonResponse(return_message)

def sign_up(request):
    args = None
    if request.method == 'POST':
        form = SignUpCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(reverse('brenda:login'))
    else:
      form = SignUpCreationForm()
      args = {'form': form}

    return render(request, 'brenda/sign_up.html', args)

# def bio(request):
#     bio = Biography.objects.all()
#     print('----'* 100)
#     print(bio)
    #
    # return render(request, 'brenda/home.html', {'bio':bio})

# def skill(request):
#     skills = Skills.objects.all()
#     print(skill)
    # return render(request, 'brenda/home.html', {'skills':skills})


# def truncate_skills(request, table_name):
#     if request.user.is_staff:
#         try:
#             # Get the model class associated with the table name
#             model_class = apps.get_model(app_label='brenda', model_name=table_name)
#
#             # Truncate the table associated with the model
#             with connection.cursor() as cursor:
#                 cursor.execute(f'TRUNCATE TABLE {model_class._meta.db_table} RESTART IDENTITY CASCADE')
#
#             return HttpResponse(f'{table_name} table truncated successfully.')
#         except LookupError:
#             return HttpResponse(f'Table {table_name} not found.', status=404)
#     else:
#         return HttpResponse("Permission denied.", status=403)
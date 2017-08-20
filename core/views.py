from django.shortcuts import render
from django.core.mail import send_mail
from .models import *


def home(request):
    data = {
        'presentation': Content.objects.get(content_id__exact='cards_apresentacao').html_text
    }
    return render(request, 'core/home.html', data)


def about(request):
    epic_about = Content.objects.get(content_id__exact='epic_about')
    coordenadorias_about = Content.objects.get(content_id__exact='coordenadorias_about')
    data = {
        'about_headline': epic_about.headline,
        'about_html': epic_about.html_text,
        'divisions_headline': coordenadorias_about.headline,
        'divisions_html': coordenadorias_about.html_text
    }
    return render(request, 'core/about.html', data)


def team(request):
    data = {
        'current': Members.objects.filter(status__istartswith='A').order_by('full_name'),
        'past': Members.objects.filter(status__istartswith='I').order_by('full_name')
    }
    return render(request, 'core/team.html', data)


def supporters(request):
    plans = Plan.objects.all()
    data = {
        'plans_continuous': plans.filter(type=PlanType.objects.get(type__exact='Contínuo')),
        'plans_workshop': plans.filter(type=PlanType.objects.get(type__exact='Workshop')),
        'plans_donation': plans.filter(type=PlanType.objects.get(type__exact='Doação')),
        'supporters': Supporters.objects.filter(
            plan__type=PlanType.objects.get(type__exact='Contínuo')).filter(status__exact='AT')
    }
    return render(request, 'core/supporters.html', data)


def contact(request):
    data = {'email_success': None}

    if request.method == 'POST':
        name = request.POST['name']
        email = str(name).title() + " <" + request.POST['email'] + ">"
        subject = "[VIA SITE] " + request.POST['subject']
        content = request.POST['message']

        company = request.POST.get('company', False)
        if company:
            content = content + '\n\n----- \n' + name + '\n' + company + '\n' + email
        else:
            content = content + '\n\n----- \n' + name + '\n' + email

        response = send_mail(subject, content, email, ['epic.ufscar@gmail.com'])

        if response == 1:
            data['email_success'] = True
        else:
            data['email_success'] = False

    else:
        data['email_success'] = None

    return render(request, 'core/contact.html', data)
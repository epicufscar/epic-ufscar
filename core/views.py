from django.db.models import Q
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
    plans = Plan.objects.all().order_by('price')
    data = {
        'plans_continuous': plans.filter(type=PlanType.objects.get(type__exact='Contínuo')),
        'plans_workshop': plans.filter(type=PlanType.objects.get(type__exact='Workshop')),
        'plans_donation': plans.filter(type=PlanType.objects.get(type__exact='Doação')),
        'supporters': Supporters.objects.filter(status__exact='AT')
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


def courses(request):
    open_applications = Workshop.objects.filter(Q(status='IA') | Q(status='VP'))
    coming_workshops = Workshop.objects.filter(status__exact='EB')
    active_workshops = Workshop.objects.filter(status__exact='EA')
    past_workshops = Workshop.objects.filter(status__exact='EN')
    workshop_groups = WorkshopGroupClass.objects.all()
    data = {
        'open_applications': open_applications,
        'coming_workshops': coming_workshops,
        'active_workshops': active_workshops,
        'past_workshops': past_workshops,
        'workshop_groups': workshop_groups
    }
    return render(request, 'core/courses.html', data)


def sprocess_2017_1(request):
    sprocess = SelectionProcess.objects.get(id__istartswith='2017.1')
    phases = SelectionProcessStep.objects.filter(process=sprocess.id).order_by('id')
    data = {
        'process': sprocess,
        'phases': phases
    }
    return render(request, 'core/sprocesses/sprocess_2017_1.html', data)


def sprocess_2018(request):
    sprocess = SelectionProcess.objects.get(id__istartswith='2018')
    phases = SelectionProcessStep.objects.filter(process=sprocess.id).order_by('id')
    data = {
        'process': sprocess,
        'phases': phases
    }
    return render(request, 'core/sprocesses/sprocess_2018.html', data)

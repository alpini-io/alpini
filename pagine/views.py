from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from django.utils import timezone
import datetime

from . models import Pagina
from .forms import ContattoForm
# Create your views here.

def contatto(request):
    submitted = False
    if request.method == 'POST':
        form = ContattoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.smtp.EmailBackend')
            messaggio = (cd['nome'] + "\n \n il giorno, " + str(timezone.make_aware(datetime.datetime.now(),timezone.get_default_timezone())) + ", ha inviato: \n \n"+cd['messaggio'] + "\n \n Il messaggio è stato inviato tramite il sito alpini.io. \n \n Nel caso, rispondere usando il seguente indirzzo email: \n \n"+cd['email'] + "\n \n ©2022 alpini.io - Gruppo Alpini Bareggio.")
            send_mail(cd['argomento'], messaggio, 'broadcast@alpini.io', ['info@alpini.io', cd['email'],],
            connection=con
            )

            return HttpResponseRedirect('/contatto?submitted=True')
    else:
            form = ContattoForm()
            if 'submitted' in request.GET:
                submitted = True

    return render (request, 'pagine/contatto.html', {
        'form': form, 'page_list': Pagina.objects.all(), 'submitted': submitted
        })
        

def index(request, paginaname):
    paginaname = '/' + paginaname
    pg = get_object_or_404 (Pagina, permalink=paginaname)
    context = {
        'titolo': pg.titolo,
        'contenuto': pg.testo,
        'aggiornato': pg.aggiornamento,
        'elenco_pagine': Pagina.objects.all(),
        }
#    return HttpResponse ("<p> testing </p>")
    return render(request, 'pagine/pagina.html', context)
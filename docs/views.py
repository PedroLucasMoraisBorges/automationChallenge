from django.shortcuts import render
from django.views import View
from .models import *
from .forms import*
from logs.models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status

from datetime import datetime

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import threading

# Functions 
def send_email_accepted(request, doc : Docs):
    def threadingFunction():
        subject = 'Documento Aprovado'
        body = render_to_string(
            './components/emails/approvedDocument.html',
            {
                'doc': doc,
            }
        )
        EmailMessage(to = ['pedrulucas000@gmail.com'], subject = subject, body = body).send()

    email_thread = threading.Thread(target=threadingFunction)
    email_thread.start()

    return Response({'message': 'Requisição aprovada com sucesso'}, status=status.HTTP_200_OK)

def send_email_denied(request, doc : Docs):
    def threadingFunction():
        subject = 'Documento Negado'
        body = render_to_string(
            './components/emails/deniedDocument.html',
            {
                'doc': doc,
            }
        )
        EmailMessage(to = ['pedrulucas000@gmail.com'], subject = subject, body = body).send()

    email_thread = threading.Thread(target=threadingFunction)
    email_thread.start()

    return Response({'message': 'Requisição aprovada com sucesso'}, status=status.HTTP_200_OK)


# Create your views here.
class DocsView(View):
    def get(self, request):
        acceptedDocuments = Docs.objects.filter(accepted=True)
        deniedDocuments = Docs.objects.filter(accepted=False)

        context = {
            'accepted': acceptedDocuments,
            'denied': deniedDocuments
        }

        return render(request, 'docs.html', context)

class RegisterDocAccepted(APIView):
    def post(self, request):
        data_dict = request.POST.dict()

        dt_register_str = data_dict['dtRegister']
        dt_register = datetime.fromisoformat(dt_register_str.replace('Z', '+00:00'))

        data_dict['dtRegister'] = dt_register

        form = DocForm(data_dict)

        if form.is_valid():
            doc = form.save(commit=False)
            doc.accepted = True
            doc.save()

            Log.objects.create(
                status = "arquivo aceito",
                description = f"Documento: {doc.docName}, autor: {doc.author}, score: {doc.score:.2f}",
                dtLog = datetime.now()
            ).save()
            
            send_email_accepted(request, doc)

        return HttpResponse("Documento Aceito cadastrado")
    
class RegisterDocDenied(APIView):
    def post(self, request):
        data_dict = request.POST.dict()

        dt_register_str = data_dict['dtRegister']
        dt_register = datetime.fromisoformat(dt_register_str.replace('Z', '+00:00'))

        data_dict['dtRegister'] = dt_register

        form = DocForm(data_dict)

        if form.is_valid():
            doc = form.save(commit=False)
            doc.accepted = False
            doc.save()

            Log.objects.create(
                status = "arquivo negado",
                description = f"Documento: {doc.docName}, autor: {doc.author}, score: {doc.score:.2f}",
                dtLog = datetime.now()
            ).save()

            send_email_denied(request, doc)

        return HttpResponse("Documento Negado cadastrado")
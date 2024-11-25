from django.shortcuts import render
from django.views import View
from .models import *
from .forms import*

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status

from datetime import datetime

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import threading
from automationChallenge.settings import EMAIL_ADMIN

# functions
def send_email_error(request, log : Log):
    def threadingFunction():
        subject = 'Erro no fluxo'
        body = render_to_string(
            './components/emails/error.html',
            {
                'log': log,
            }
        )
        EmailMessage(to = [EMAIL_ADMIN], subject = subject, body = body).send()

    email_thread = threading.Thread(target=threadingFunction)
    email_thread.start()
    return Response({'message': 'Requisição aprovada com sucesso'}, status=status.HTTP_200_OK)


# Create your views here.
class Logs(View):
    def get(self, request):
        logs = Log.objects.filter()

        context = {
            'logs' : logs
        }

        return render(request, 'logs.html', context)

class RegisterLog(APIView):
    def post(self, request):
            data_dict = request.POST.dict()

            form = LogForm(data_dict)

            if form.is_valid():
                log = form.save(commit=False)
                log.dtLog = datetime.now()
                log.save()
                
                send_email_error(request, log)

            return HttpResponse("Documento Aceito cadastrado")
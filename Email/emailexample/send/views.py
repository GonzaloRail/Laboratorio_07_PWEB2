from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def index(request):
    send_mail('Prueba',
    'Probando el envio de email',
    'azel987654321@gmail.com',#El que envia 
    ['glaymem@unsa.edu.pe'],#El que recibe
    fail_silently=False
    )



    return render(request, 'send/index.html')
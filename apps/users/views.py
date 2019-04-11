from django.shortcuts import render, redirect
from apps.users.models import User
#from django.core.mail import EmailMessage
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

def addUsers(request):
    if request.method == "POST":
        statement = User(user=request.POST.get('user'), password=request.POST.get('password'), email=request.POST.get('email'))
        statement.save()
        sta = 'user: ' + request.POST.get('user') + ' and password: ' + request.POST.get('password') + ' Has sido Guardados'
        title = 'Registro de usuario nuevo'
        body = 'se ha Creado un nuevo usuario para usted, llamado: '+request.POST.get('user')+' y su password es: '+request.POST.get('password') + ', muchas gracias, atentamente BrayanDev'
        email_send = request.POST.get('email')
        #settings.DEFAULT_FROM_EMAIL = 'developerbrayan@gmail.com'
        #email_send_now = settings.DEFAULT_FROM_EMAIL
        #email = EmailMessage(title, body, to=[email_send])
        #email.send()
        #context = {'guardado':'Guardado'}

        email = request.POST.get('email', None)
        subject = 'Registro'
        message = 'Bienvenido, hemos creado tu cuenta.'
        context = {'body':body, 'email': email, 'subject': subject, 'message': message, 'user':request.POST.get('user'), 'password':request.POST.get('password')}

        html_message = render_to_string('template_email/email.html', {'context': context})
        plain_message = strip_tags(html_message)

        send_mail(title, plain_message, settings.EMAIL_HOST_USER,
                  [email_send], html_message=html_message, fail_silently=False)

        return render(request, 'users/add_users.html', {'sta':body})
    return render(request, 'users/add_users.html')

def users(request):
    user = User.objects.all().order_by('-id')
    context = {'users':user}
    return render(request, 'users/users.html', context)

def editUser(request):
    if request.method == "POST":
        title = 'actualizacion de datos de ingreso de la cuenta'
        body = 'se ha cambiado sus datos de acceso: usuario ' + request.POST.get(
            'user') + ' y su password es: ' + request.POST.get('password') + ', atentamente BrayanDev'
        subject = 'Su cuenta ha Sido Actualizada'
        message = 'hemos Actualizado su cuenta.'

        user = User.objects.filter(id=request.POST.get('id')).update(user=request.POST.get('user'),
                                                                     password=request.POST.get('password'),
                                                                     email=request.POST.get('email'))
        context = {'update': 'Usuario Editado', 'body': body, 'email': request.POST.get('email'), 'subject': subject,
                   'message': message, 'user': request.POST.get('user'),
                   'password': request.POST.get('password')}

        html_message = render_to_string('template_email/email.html', {'context': context})
        plain_message = strip_tags(html_message)

        send_mail(title, plain_message, settings.EMAIL_HOST_USER,
                  [request.POST.get('email')], html_message=html_message, fail_silently=False)

        return render(request, 'users/users.html', context)


def deleteUser(request):
    if request.method == 'GET':
        delete_user = User.objects.filter(id=request.GET.get('id')).delete()
        context = {'deleteUser':delete_user}
        return redirect('/users', context)

from django.shortcuts import render
import random
# from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'generador/home.html')


def about(request):
    return render(request, 'generador/about.html')


def password(request):
    caracteres = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    # Convierte un string en int, utiliza la propiedad GET.get de request y utiliza el valor que contenga la clave 'length'
    longitud = int(request.GET.get('length'))

    # Permite utilizar mayusculas si el usuario marco la opcion, si marca la opcion de mayuscula, retorna un valor booleano. Luego extiende la lista añadiendo caracteres en mayuscula
    if request.GET.get('uppercase'):
        caracteres.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        caracteres.extend(list('!|#$%&/()=?¿¡\\_-:@'))

    if request.GET.get('numbers'):
        caracteres.extend(list('0123456789'))

    # Almacena una serie de caracteres aleatorios de la lista.
    for i in range(longitud):
        generated_password += random.choice(caracteres)

    # Muestra el archivo html en la url y pasa como parametro al diccionario con clave y valor
    return render(request, 'generador/password.html', {'password': generated_password})

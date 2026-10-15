from django.shortcuts import render
from .models import Usuario

def mostrar_login(request):
    return render(request, 'login.html')

def index(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre_apellido")
        usuario_form = request.POST.get("usuario")
        gmail = request.POST.get("gmail")
        password_form = request.POST.get("password")

        nuevo_usuario = Usuario(
            nombre_apellido=nombre,
            usuario=usuario_form,
            gmail=gmail,
            password=password_form
        )
        nuevo_usuario.save()

        datos = {
            "nombre": nombre,
            "gmail": gmail,
            "usuario": usuario_form
        }
        return render(request, "pagina.html", datos)
    
    return render(request, 'login.html')

def login2(request):
    if request.method == "POST":
        usuario_ingresado = request.POST.get("usuario")
        password_ingresada = request.POST.get("password")

        usuario_db = Usuario.objects.filter(
            usuario=usuario_ingresado, 
            password=password_ingresada
        ).first()

        if usuario_db:
            datos = {
                "nombre": usuario_db.nombre_apellido,
                "gmail": usuario_db.gmail,
                "usuario": usuario_db.usuario
            }
            return render(request, "pagina.html", datos)
        else:
            return render(request, "error.html", {"error": "Usuario o contraseña incorrectos."})

    return render(request, 'login2.html')
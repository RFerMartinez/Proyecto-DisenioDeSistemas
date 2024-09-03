from django.shortcuts import render

# Vista basada en función para el home
def home(request):
    template="home.html"
    ctx = {

    }
    return render(
        request=request,
        template_name=template,
        context=ctx
    )

def IniciarSesion(request):
    template="IniciarSesion.html"
    ctx = {

    }
    return render(
        request=request,
        template_name=template,
        context=ctx
    )

def Registrarse(request):
    template="Registrarse.html"
    ctx = {

    }
    return render(
        request=request,
        template_name=template,
        context=ctx
    )

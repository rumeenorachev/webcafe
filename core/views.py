from django.shortcuts import render
from .forms import ContactForm
from .models import Mensaje


# Create your views here.

def index(request):
    return render(request, "core/index.html")
def about(request):
    return render(request, "core/about.html")
def services(request):
    return render(request, "core/services.html")
def store(request):
    return render(request, "core/store.html")
#def contact(request):
    #return render(request, "core/contact.html")
def blog(request):
    return render(request, "core/blog.html")
def privacidad(request):
    return render(request, "core/privacidad.html")
def cookies(request):
    return render(request, "core/cookies.html")
def aviso(request):
    return render(request, "core/aviso.html")

def contact(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            # Guardar en base de datos
            Mensaje.objects.create(
                nombre=form.cleaned_data['nombre'],
                email=form.cleaned_data['email'],
                mensaje=form.cleaned_data['mensaje']
            )

            # Reiniciar el formulario
            form = ContactForm()

            return render(request, 'core/contact.html', {
                'form': form,
                'mensaje_enviado': True
            })

    return render(request, 'core/contact.html', {'form': form})
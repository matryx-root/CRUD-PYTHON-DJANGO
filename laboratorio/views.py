from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from laboratorio.forms import LaboratorioForm
from laboratorio.models import Laboratorio


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('laboratorio:home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def laboratorio(request):
    # Obtiene todos los objetos Laboratorio desde la base de datos
    laboratorios = Laboratorio.objects.all()

    # Puedes agregar más lógica aquí para procesar los datos si es necesario

    # Crea un diccionario con los datos que quieres pasar a la plantilla
    contexto = {
        'laboratorios': laboratorios,
    }

    # Renderiza la plantilla 'laboratorio.html' con el contexto dado
    return render(request, 'laboratorio.html', contexto)


def actualizar_contador_visitas(request):
    contador_visitas = request.session.get('contador_visitas', 0)
    contador_visitas += 1

    # Guardar el contador de visitas en la sesión
    request.session['contador_visitas'] = contador_visitas

    return contador_visitas


def home(request):
    contador_visitas = actualizar_contador_visitas(request)

    return render(request, 'home.html', {'contador_visitas': contador_visitas})


def mostrar_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    contador_visitas = request.session.get('contador_visitas', 0)
    contador_visitas += 1
    request.session['contador_visitas'] = contador_visitas

    return render(request, 'mostrar.html', {'laboratorios': laboratorios, 'contador_visitas': contador_visitas})


@login_required
def insertar_laboratorio(request):
    if request.method == 'POST':
        # Procesar el formulario enviado
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            # Redireccionar a la página de mostrar laboratorios
            return redirect('laboratorio:mostrar')
    else:
        # Mostrar el formulario vacío
        form = LaboratorioForm()

    # Llama a la función para actualizar el contador de visitas
    contador_visitas = actualizar_contador_visitas(request)

    return render(request, 'laboratorio/insertar.html', {'form': form})


@login_required
def editar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, pk=laboratorio_id)

    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            # Reemplaza 'laboratorio:mostrar' con el nombre de la URL para mostrar todos los laboratorios
            return redirect('laboratorio:mostrar')
    else:
        form = LaboratorioForm(instance=laboratorio)

    return render(request, 'editar.html', {'form': form})


@login_required
def eliminar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, pk=laboratorio_id)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('laboratorio:mostrar')
    return render(request, 'eliminar.html', {'laboratorio': laboratorio})

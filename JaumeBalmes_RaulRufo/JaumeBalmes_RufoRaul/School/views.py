from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader
from .forms import PersonaForm
from .models import Person

'''
profes = [
    {
        'id':'1',
        'name': 'Roger',
        'surname': 'Sobrino',
        'age': 41,
    },
    {
        'id':'2',
        'name': 'Oriol',
        'surname': 'Roca',
        'age': 35,
    },
    {
        'id':'3',
        'name': 'Juanma',
        'surname': 'Sanchez',
        'age': 38,
    }
]
alums = [
    {
        'id':'1',
        'name': 'Raul',
        'surname': 'Rufo',
        'age': 19,
    },
    {
        'id':'2',
        'name': 'Matias',
        'surname': 'Rodriguez',
        'age': 20,
    },
    {
        'id':'3',
        'name': 'Javi',
        'surname': 'Miranda',
        'age': 21,
    },
    {
        'id':'4',
        'name': 'Raymon',
        'surname': 'Vega',
        'age': 22,
    },
    {
        'id':'5',
        'name': 'Jonathan',
        'surname': 'Valle',
        'age': 19,
    },
    {
        'id':'6',
        'name': 'Joan',
        'surname': 'Jimenez',
        'age': 27,
    },
]
'''

def index(request):
    datosCentro = {
            'name': 'JaumeBalmes',
            'direccion': 'Antonio Valverde',
            'ubicacion': 'Pau Claris con Balmes',
        }
    return render(request,'index.html', {'Nombre': datosCentro['name'],
                                         'Direccion': datosCentro['direccion'],
                                         'Ubicacion': datosCentro['ubicacion']
                                        })


def alumnos(request):

    context = {'alums':alums}
    return render(request, 'alum/alumnos.html', context)

def alumno(request, pk):
    alumno_Obj = None
    for i in alums:
        if i['id'] == pk:
            alumno_Obj = i
    return render(request, "alum/alumno.html",{'alums':alumno_Obj})

def profesores(request):
    context = {'profes':profes}
    return render(request, 'prof/profesores.html', context)

def profesor(request, pk):
    profesor_Obj = None
    for i in profes:
        if i['id'] == pk:
            profesor_Obj = i
    return render(request, 'prof/profesor.html',{'profes':profesor_Obj})


#def userForm(request):
#    form = PersonaForm()
#    context = {'form':form}
#    return render(request, 'formularios/form.html', context)

def userForm(request):
    form = PersonaForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index_one')
    context = {'form':form}
    return render(request, 'formularios/form.html', context)

def users(request):
    usuarios = Person.objects.all()
    context = {'users':usuarios}
    return  render(request, 'crud/users.html', context)

def update_users(request, pk):
    person = Person.objects.get(id=pk)
    form = PersonaForm(instance=person)

    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('index_one')
    context = {'form': form}
    return render(request, 'formularios/form.html', context)

def delete_users(request, pk):
    person = Person.objects.get(id=pk)
    if request.method == 'POST':
        person.delete()
        return redirect('index_one')
    context = {'object':person}
    return render(request, 'formularios/delete_object.html', context)

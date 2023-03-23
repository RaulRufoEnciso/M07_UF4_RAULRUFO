from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
profes = [
        {
            'name': 'Roger',
            'surname': 'Sobrino',
            'age': 41,
        },
        {
            'name': 'Oriol',
            'surname': 'Roca',
            'age': 35,
        }
    ]
alums = [
    {
        'name': 'Raul',
        'surname': 'Rufo',
        'age': 19,
    },
    {
        'name': 'Matias',
        'surname': 'Rodriguez',
        'age': 20,
    },
{
        'name': 'Javi',
        'surname': 'Rufo',
        'age': 19,
    },
    {
        'name': 'Matias',
        'surname': 'Rodriguez',
        'age': 20,
    },
{
        'name': 'Raul',
        'surname': 'Rufo',
        'age': 19,
    },
    {
        'name': 'Matias',
        'surname': 'Rodriguez',
        'age': 20,
    },
]

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

# Error
def alumnos(request):

    context = {'alums':alums}
    return render(request, 'alum/alumnos.html', context)

def profesores(request):
    template = loader.get_template('prof/profesores.html')
    return HttpResponse(template.render())
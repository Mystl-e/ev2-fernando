from django.shortcuts import render, get_object_or_404
from django.http import Http404


def _peliculas(lista):
    return [
        {'nombre': n, 'anio': a, 'imagen': f'images/peliculas/{img}'}
        for n, a, img in lista
    ]


GENEROS = [
    {
        'slug': 'accion',
        'nombre': 'Acción',
        'descripcion': 'Persecuciones, combates y mucha adrenalina.',
        'peliculas': _peliculas([
            ('Mad Max: Fury Road', 2015, 'mad-max.jpg'),
            ('John Wick', 2014, 'john-wick.jpg'),
            ('Die Hard', 1988, 'die-hard.jpg'),
            ('The Dark Knight', 2008, 'dark-knight.jpg'),
            ('Gladiator', 2000, 'gladiator.jpg'),
            ('Mission: Impossible - Fallout', 2018, 'mi-fallout.jpg'),
            ('Matrix', 1999, 'matrix.jpg'),
            ('Casino Royale', 2006, 'casino-royale.jpg'),
            ('Top Gun: Maverick', 2022, 'top-gun.jpg'),
            ('Terminator 2', 1991, 'terminator-2.jpg'),
        ]),
    },
    {
        'slug': 'ciencia-ficcion',
        'nombre': 'Ciencia Ficción',
        'descripcion': 'Futuros posibles, tecnología y exploración espacial.',
        'peliculas': _peliculas([
            ('Blade Runner 2049', 2017, 'blade-runner.jpg'),
            ('Interestelar', 2014, 'interestelar.jpg'),
            ('Inception', 2010, 'inception.jpg'),
            ('Dune', 2021, 'dune.jpg'),
            ('Arrival', 2016, 'arrival.jpg'),
            ('Ex Machina', 2014, 'ex-machina.jpg'),
            ('Alien', 1979, 'alien.jpg'),
            ('Star Wars: Episodio IV', 1977, 'star-wars.jpg'),
            ('Gravity', 2013, 'gravity.jpg'),
            ('Minority Report', 2002, 'minority-report.jpg'),
        ]),
    },
    {
        'slug': 'drama',
        'nombre': 'Drama',
        'descripcion': 'Historias intensas centradas en emociones y personajes.',
        'peliculas': _peliculas([
            ('Cadena perpetua', 1994, 'cadena-perpetua.jpg'),
            ('El padrino', 1972, 'el-padrino.jpg'),
            ('Forrest Gump', 1994, 'forrest-gump.jpg'),
            ('Parásitos', 2019, 'parasitos.jpg'),
            ('Whiplash', 2014, 'whiplash.jpg'),
            ('La La Land', 2016, 'la-la-land.jpg'),
            ('El club de la pelea', 1999, 'club-pelea.jpg'),
            ('Moonlight', 2016, 'moonlight.jpg'),
            ('Una mente brillante', 2001, 'mente-brillante.jpg'),
            ('Oppenheimer', 2023, 'oppenheimer.jpg'),
        ]),
    },
]


def inicio(request):
    return render(request, 'home_fernando/inicio.html', {'generos': GENEROS})


def genero_detalle(request, slug):
    genero = next((g for g in GENEROS if g['slug'] == slug), None)
    if genero is None:
        raise Http404('Género no encontrado')
    return render(request, 'home_fernando/genero.html', {'genero': genero})
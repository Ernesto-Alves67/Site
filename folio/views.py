from django.shortcuts import render


def index(request):
    context = {'page': request.path}
    return render(request, 'folio/index.html', context)


def educacao(request):
    context = {'page': request.path}
    return render(request, 'folio/edu.html', context)


def experiencia(request):
    context = {'page': request.path}
    return render(request, 'folio/xp.html', context)


def skills(request):
    context = {'page': request.path}
    return render(request, 'folio/skills.html', context)


def projects(request):
    context = {'page': request.path}
    return render(request, 'folio/projetos.html', context)


def interesses(request):
    context = {'page': request.path}
    return render(request, 'folio/interesses.html', context)

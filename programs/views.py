from django.shortcuts import render, redirect
from .models import Prog


def programs_list(request):
    prog = Prog.objects.all()
    ctx = {'prog': prog}
    return render(request, 'programs/programs-list.html', ctx)


def programs_form(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    if name and description:
        Prog.objects.create(
        name=name,
        description=description,
    )
        return redirect('programs:app')
    return render(request, 'programs/programs-form.html')


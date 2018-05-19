# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Recette

# Create your views here.
def recettes(request):
    recettes = Recette.objects.all()
    context = {
        'recettes' : recettes
    }
    return render(request, 'recettes.html', context)
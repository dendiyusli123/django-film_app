# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import (ListView, DetailView,)
from film_app.models import Film 

class FilmList(ListView):
    model = Film

class FilmDetail(DetailView):
    model = Film

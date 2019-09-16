from django.shortcuts import render
from django.views.generic import ListView

from .models import Term


class TermListView(ListView):
    model = Term
    template_name = "termlist.html"


# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime
from random import randint
from find_path import *


# Create your views here.


def home_page(request):
    context = {}
    template = "home_page.html"
    n_columns = 6


    randon_matrix = generate_matrix(n_columns)

    if(request.POST):
        matrix = get_matrix_from_template(request.POST, n_columns)
        graph = generate_graph(matrix)
        path = shortest_path(graph, matrix[1][1], matrix[n_columns][n_columns], [], {}, {})

        context['matrix'] = matrix
        context['total'] = path[0]
        context['result'] = path[1]
    else:
        context['matrix'] = randon_matrix
    

    return render_to_response(template, context, 
        context_instance=RequestContext(request))


def generate_matrix(columns):
    matrix = {}
    x = 1
    y = 1

    while x <= columns:
        matrix[x] = {}
        while y <= columns:
            matrix[x][y] = hex(randint(100, 40000)).lstrip("0x").upper()
            y += 1
        x += 1
        y = 1

    return matrix

def get_matrix_from_template(table, size):
    matrix = {}
    x = 1
    y = 1

    while x <= size:
        matrix[x] = {}
        while y <= size:
            matrix[x][y] = str(table.get(str(x)+'_'+str(y)))
            y += 1
        x += 1
        y = 1

    return matrix


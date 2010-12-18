# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader, Context, RequestContext

from dojango.decorators import json_response
from dojango.util import dojo_collector

from movie.models import Movie
from core.forms import MovieForm, DojoMovieForm
from core.stores import MPTreeStore

def show(request):
    return render_to_response("core/show.html", context_instance=RequestContext(request))

def show_form(request, id):
    movie = Movie.objects.get(id=id)
    form = DojoMovieForm(instance=movie)
    default_form = MovieForm(instance=movie)
    return render_to_response("core/show_form.html", locals(), context_instance=RequestContext(request))

def show_tab_container(request):
    dojo_collector.add_module("dijit.layout.ContentPane")
    dojo_collector.add_module("dijit.layout.TabContainer")
    return render_to_response("core/show_tab_container.html", locals(), context_instance=RequestContext(request))

def show_tree(request):
    store = MPTreeStore()
    return HttpResponse(store.to_json(), mimetype='application/json')
    
def dojo_tree(request):
    return render_to_response("core/tree_test.html", locals(), context_instance=RequestContext(request))

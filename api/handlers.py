from piston.handler import BaseHandler, AnonymousBaseHandler

import movie
from movie.models import Movie
import re

BaseHandler.fields = AnonymousBaseHandler.fields = ()

class MovieHandler(BaseHandler):
    allowed_methods = ('GET','PUT',)
    model = Movie
    exclude = ()

    def read(self, request, id=None):
        base = Movie.objects
        try:
            int(id)
            if id:
                return base.get(id=id)
            else:
                return base.all()
        except:
            return base.all()
        

class MovieActorHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Movie
    exclude = ()
    
    def read(self, request, id):
        movie = Movie.objects.get(id=id)
        return movie.actors.all()

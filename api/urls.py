from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view

from handlers import MovieHandler, MovieActorHandler

movie_resource = Resource(handler=MovieHandler)
movie_actor_resource = Resource(handler=MovieActorHandler)

urlpatterns = patterns('',
    url(r'^movies/$', movie_resource),
    url(r'^movies/(?P<id>.+)/actors/$', movie_actor_resource),
    url(r'^movies/(?P<id>.+)$', movie_resource),
)

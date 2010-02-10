from django.forms.models import ModelForm
from dojango.forms.models import ModelForm as DojoModelForm

from dojango.forms import fields, widgets
from dojango.forms.models import ModelChoiceField

from movie.models import Movie, Director

class MovieForm(ModelForm):
    class Meta:
        model = Movie

class DojoMovieForm(DojoModelForm):
    plot = fields.CharField(widget=widgets.EditorInput(attrs={"height": "auto"}))
    rating = fields.DecimalField(widget=widgets.HorizontalSliderInput, max_value=10)

    class Meta:
        model = Movie

class DojoDirectorForm(DojoModelForm):
    movie = fields.ModelChoiceField(Director.objects.all(), widget=widgets.FilteringSelectStore(url="blubb"))
    
    class Meta:
        model = Director
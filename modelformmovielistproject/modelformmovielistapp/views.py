from django.shortcuts import render
from modelformmovielistapp.forms import movieform


# Create your views here.
def movielistview(request):
    movies = movieform()
    return render(request,'modelformovielistapp/list.html',{'movies': movies})

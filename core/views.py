# Create your views here.
from django.shortcuts import render
from .forms import urlentry
from . webmodel import scrape
def showform(request):
    if request.method == 'POST':
        form = urlentry(request.POST)
        if form.is_valid():
            # Process the form data
            names=form.cleaned_data['name']
            urls= form.cleaned_data['url']
            response=scrape(urls,names)
        return response
            
    else:
        form = urlentry()
    return render(request, 'core/base.html', {'form': form})

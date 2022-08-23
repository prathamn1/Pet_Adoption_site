from urllib import request
from django.shortcuts import render
from .models import Pet


# Create your views here.
from django.http import Http404 # to give http response from our view

def home(request):
    pets=Pet.objects.all()
    return render(request,'home.html',{
        'pets':pets,
        })

# render(requests,  string for name of tempelate ,  dictionary with the data we want to be available inside a tempelate , the keys are need to be string and are used inside the tempelate as variable names)

def pet_detail(request,pet_id): # creating views
    # return HttpResponse(f'<p> pet_detail view with id {pet_id} </p>')
    try: # so when some one gives id which is beyond our range
        pet=Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('Pet not Found. Try a different one instead !') #raises a 404 error
    return render(request,'pet_detail.html',{
        'pet':pet,
        })


# general convention is to name a tempelate file with respective views



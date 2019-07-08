from django.http import HttpResponse
from django.shortcuts import render, redirect
from labeling.models import Content, Decision
from random import randint



# importing loading from django template
from django.template import loader


# our view which is a function named index
def labelView(request):

    #loading the data
    numberOfObjects = Content.objects.count()
    randomIndex = randint(1, numberOfObjects)
    object = Content.objects.get(id=randomIndex)

    context = {
        'text': object
    }
    # rendering the template in HttpResponse
    return render(request, 'label.html', context)

def vote(request, content_id, vote_key):
    d = Decision(decisionNumber=vote_key, content_id=content_id)
    d.save()
    return redirect('index')


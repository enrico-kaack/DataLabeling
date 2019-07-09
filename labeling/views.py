from django.http import HttpResponse
from django.shortcuts import render, redirect
from labeling.models import Content, Decision
from random import randint
import csv



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

def resultView(request):
    if request.user.is_superuser:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="results.csv"'

        writer = csv.writer(response)
        writer.writerow(['identifier', 'result'])
        d = Decision.objects.all()
        for decision in d:
            writer.writerow([decision.content.meta_data, decision.decisionNumber])

        return response
    else:
        return HttpResponse(403)
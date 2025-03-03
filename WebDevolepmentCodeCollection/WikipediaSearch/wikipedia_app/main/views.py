from django.http import HttpResponse
from django.shortcuts import render, resolve_url
import wikipedia

def home(request):
    if request.method == "POST":
        search = request.POST['search']
        try:
            result = wikipedia.summary(search, sentences = 3) # No of sentences that you want as output
        except:
            return HttpResponse("Wrong Input")
        return render(request, "main/index.html",{"result":result})
    return render(request, 'main/index.html')

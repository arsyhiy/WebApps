from django.http.response import HttpResponse
from django.shortcuts import render
from translate import Translator, translate


def home(request):
    if request.method == "POST":
        text = request.POST["translate"]
        language = request.POST['language']
        translator = Translator(to_lang=language)
        translation = translator.translate(text)
        return HttpResponse(translation)
    return render(request, "main/index.html")

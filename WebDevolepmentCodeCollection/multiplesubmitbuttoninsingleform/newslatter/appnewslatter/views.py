from django.shortcuts import render
from django.contrib import messages
from .models import newslattermail
 
def home(request):
     
    # if post request comes from the subscribe button
    # then saving user email in our database
    if 'subscribe' in request.POST:
        email = newslatteremail()
        email.userEmail = request.POST.get("email")
        email.save()
        messages.info(
            request, 'You have successfully subscribed to our newslatter.')
     
    # if post request comes from the unsubscribe button
    # then deleting the user email from our database
    if 'unsubscribe' in request.POST:
        newslatteremail.objects.get(
            userEmail=request.POST.get("email")).delete()
        messages.info(request, 'sorry to see you!!!')
         
    return render(request, 'news.html')


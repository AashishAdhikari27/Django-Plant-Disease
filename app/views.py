from django.shortcuts import render,  redirect, get_object_or_404
from django.conf import settings




def home(request):

    # Define your message
    message = "Welcome to our Plant Leaf Diseases Classifier System !!"
    
    # Pass the message to the template context
    return render(request, 'app/home.html', {'message': message})


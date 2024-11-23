from django.shortcuts import render,  redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from .forms import ImageUploadForm




def home(request):

    # Define your message
    message = "Welcome to our Plant Leaf Diseases Classifier System !!"
    
    # Pass the message to the template context
    return render(request, 'app/home.html', {'message': message})




def predict(request):

    if request.method == 'POST' and request.FILES['image']:

        uploaded_image = request.FILES['image']
        print(uploaded_image)

        # Process the image (save to disk, etc.)
        return HttpResponse('Image uploaded successfully!')
    
    return render(request, 'home.html')
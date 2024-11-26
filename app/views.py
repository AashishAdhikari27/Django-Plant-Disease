from django.shortcuts import render,  redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse,JsonResponse
from .forms import ImageUploadForm



import tensorflow as tf
import os 
import numpy as np
from PIL import Image
import json

# from tensorflow.keras.models import load_model



# loading the model 

# model = load_model('models/plant_disease_prediction_model.h5')  # Replace with the actual model path


model_path = "models/plant_disease_prediction_model.h5"  
model = tf.keras.models.load_model(model_path)



# Loading the class indices
class_indices_path= os.path.join(settings.BASE_DIR, 'class_indices.json')
with open(class_indices_path, 'r') as file:
    class_indices = json.load(file)
class_names = {v: k for k, v in class_indices.items()}  # Reverse the mapping to get class names




# image preprocessing function
def preprocess_image(image, target_size=(224, 224)):
    # Resize the image
    image = image.resize(target_size)
    # Convert image to array
    img_array = np.array(image)
    # Add batch dimension and normalize
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype('float32') / 255.0
    return img_array



def home(request):

    # Define your message
    message = "Welcome to our Plant Leaf Diseases Classifier System !!"


    
    # Pass the message to the template context
    return render(request, 'app/home.html', {'message': message})




# def predict(request):

#     if request.method == 'POST' and request.FILES['image']:

#         uploaded_image = request.FILES['image']
#         print(uploaded_image)

#         # Process the image (save to disk, etc.)
#         return HttpResponse('Image uploaded successfully!')
    
#     return render(request, 'home.html')




# Predict view
def predict(request):
    if request.method == 'POST' and request.FILES.get('image'):
        try:
            # Get the uploaded image
            uploaded_image = request.FILES['image']
            
            # Open the image using PIL
            image = Image.open(uploaded_image)
            
            # Preprocess the image
            preprocessed_img = preprocess_image(image)

            
            # Predict the class
            predictions = model.predict(preprocessed_img)
            predicted_class_index = np.argmax(predictions, axis=1)[0]
            predicted_class_name = class_indices[str(predicted_class_index)]
            # Return the prediction
            return JsonResponse({'prediction': predicted_class_name})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return HttpResponse('Invalid request', status=400)


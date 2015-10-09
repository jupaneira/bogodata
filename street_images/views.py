from django.shortcuts import render, redirect, get_object_or_404
from .models import Image


def images(request):
    img = Image.objects.order_by('hits')[0]
    return render(request, 'street_images/home.html', {'image': img})

def inseguro(request, pk):
    print(pk)
    image = get_object_or_404(Image, pk=pk)
    image.hits = image.hits + 1
    image.save()
    print(image.lat," *************", image.hits)
    return redirect('images')
    

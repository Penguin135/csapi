from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import OriginImage
from .models import SeparatedImage
from .forms import UploadForm

# login required
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'csapi/main.html')

@login_required(login_url='login:login')
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            origin_image = form.save(commit=False)
            origin_image.auth_user = request.user
            origin_image.save()
            origin_image_id = origin_image.id
            return redirect('csapi:origin_image_show', origin_image_id)
    else:
        form = UploadForm()
    return render(request, 'csapi/upload.html', {
        'form' : form
    })

def origin_image_show(request, image_id):
    origin_image = OriginImage.objects.get(id=image_id)
    try:
        separated_image = SeparatedImage.objects.get(origin_image_id=image_id)
    except SeparatedImage.DoesNotExist:
        separated_image = None
    return render(request, 'csapi/image_show.html', {
        'origin_image' : origin_image,
        'separated_image' : separated_image,
    })

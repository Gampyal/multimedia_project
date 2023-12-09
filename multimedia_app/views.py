


from django.shortcuts import render, redirect
from .models import MultimediaFile
from .forms import MultimediaFileForm

def file_list(request):
    files = MultimediaFile.objects.all()
    return render(request, 'multimedia_app/file_list.html', {'files': files})

def upload_file(request):
    if request.method == 'POST':
        form = MultimediaFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = MultimediaFileForm()
    return render(request, 'multimedia_app/upload_file.html', {'form': form})

from django.shortcuts import render
from django.http import HttpResponse
from .models import Request
from .forms import RequestForm
from .scripts import create_video_opencv


def post(request):
    if request.method == "POST":
        req = Request(text=request.POST['text'])
        req.save()
        create_video_opencv(request.POST['text'])
        with open('running_line.mp4', 'rb') as rl:
            response = HttpResponse(rl.read(), content_type='video/mp4')
            response['Content-Disposition'] = 'video; filename=running_line.mp4'
            return response
    else:
        form = RequestForm()
    return render(request, 'running_line/page.html', {'form': form})
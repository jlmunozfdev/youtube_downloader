from django.shortcuts import render
from pytube import YouTube
from django.http import HttpResponse

def download_video(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        response = HttpResponse(
            content_type='video/mp4',
        )
        response['Content-Disposition'] = f'attachment; filename="{yt.title}.mp4"'
        stream.stream_to_buffer(response)
        return response
    return render(request, 'index.html')

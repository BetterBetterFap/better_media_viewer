from django.shortcuts import render, HttpResponse

import os

from .models import Media


def home(request):
    return render(request, 'viewer/home.html')


image_exts = ['.jpg', ',jpeg', '.gif', '.png']
video_exts = ['.mp4']


def media(request, file_id):
    media_entry = Media.objects.get(id=file_id)
    if not Media:
        return HttpResponse('content not found')
    _, ext = os.path.splitext(media_entry.file_field.name)
    if ext in image_exts:
        context = {
            'content': media_entry,
        }
        return render(request, 'viewer/image.html', context=context)
    elif ext in video_exts:
        context = {
            'content': media_entry,
            'ext': f'video/{ext[1:]}',
        }
        return render(request, 'viewer/video.html', context=context)
    return HttpResponse(f'File format not supported {ext}')




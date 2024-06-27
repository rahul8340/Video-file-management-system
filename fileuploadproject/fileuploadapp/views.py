
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadedFile
import os
import ffmpeg



def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            uploaded_file = UploadedFile.objects.create(
                file=file,
                name=file.name,
                description=form.cleaned_data['description'],
                tags=form.cleaned_data['tags']
            )
            file_path = os.path.join('media', str(uploaded_file.file))
            probe = ffmpeg.probe(file_path)
            video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
            duration = video_info['duration']
            fps = video_info.get('avg_frame_rate')
            size = os.path.getsize(file_path)
            codec_type = video_info['codec_name']
            bitrate = int(video_info['bit_rate']) // 1000  # Convert to kbps
            resolution = f"{video_info['width']}x{video_info['height']}"
            uploaded_file.duration = duration
            uploaded_file.size = size
            uploaded_file.fps = eval(fps) if fps else None
            uploaded_file.codec_type = codec_type
            uploaded_file.bitrate = bitrate
            uploaded_file.resolution = resolution
            uploaded_file.save()
            
             
            audio_info = next(s for s in probe['streams'] if s['codec_type'] == 'audio')
            audio_codec_type = audio_info['codec_name']
            audio_channels = audio_info['channels']
            audio_sample_rate = audio_info['sample_rate']
            uploaded_file.audio_codec_type = audio_codec_type
            uploaded_file.audio_channels = audio_channels
            uploaded_file.audio_sample_rate = audio_sample_rate
            uploaded_file.save()
            
            return redirect('file_list')
    else:
        form = UploadFileForm()
    return render(request, 'fileuploadapp/upload.html', {'form': form})


from django.shortcuts import render
from .models import UploadedFile


def file_list(request):
    search_query = request.GET.get('search', '')
    files = UploadedFile.objects.filter(name__icontains=search_query)
    return render(request, 'fileuploadapp/file_list.html', {'files': files, 'search_query': search_query})

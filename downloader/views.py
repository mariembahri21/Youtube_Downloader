from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from pytube import YouTube

def index(request):
    return render(request, 'downloader/index.html')

@csrf_exempt
def download(request):
    if request.method == 'POST':
        url = request.POST['url']
        try:
            yt = YouTube(url)
            stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
            if stream:
                download_path = os.path.join('downloads', stream.default_filename)
                stream.download(output_path="C:/Users/bahri/Videos")
                return JsonResponse({'status': 'success', 'message': 'Téléchargement terminé !', 'file': download_path})
            else:
                return JsonResponse({'status': 'error', 'message': 'Aucune vidéo trouvée avec cette URL.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Méthode non autorisée.'})

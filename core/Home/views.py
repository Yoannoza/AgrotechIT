# Create your views here.
from django.shortcuts import render
from .models import Utilisateur, Projet, Tag, Photo, Video
from itertools import zip_longest
import uuid

def home(request):
    users = Utilisateur.objects.all()
    projets = Projet.objects.prefetch_related('photos', 'videos', 'tags').all()
    context = []

    for projet in projets:
        photos = list(projet.photos.all())
        videos = list(projet.videos.all())
        media = [item for pair in zip_longest(photos, videos) for item in pair if item is not None]

        

        # Générer un UUID4
        unique_id = uuid.uuid4()
        
        context.append({
            'id1': uuid.uuid4().hex,
            'id2': uuid.uuid4().hex,
            'projet': projet,
            'media': media,
            'media_count': range(len(media)),
            # 'photo_count': len(photos),
            # 'video_count': len(videos),
        })

    return render(request, 'home.html', {'users': users, 'projets_data' : context})


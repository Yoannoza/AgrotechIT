from django.contrib import admin
from .models import Utilisateur, Tag, Projet, Photo, Video


admin.site.register(Utilisateur)
admin.site.register(Projet)
admin.site.register(Tag)
admin.site.register(Photo)
admin.site.register(Video)

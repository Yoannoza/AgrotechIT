from django.db import models

# Modèle Utilisateur
class Utilisateur(models.Model):
    profil = models.ImageField(upload_to='Users')
    lastname = models.CharField(max_length=2555)
    name = models.CharField(max_length=2555)
    email = models.EmailField(unique=True)
    tel = models.IntegerField()
    job_title = models.CharField(max_length=255)
    motivation = models.TextField(blank=True, null=True)
    linkedin_url = models.CharField(max_length=2555, blank=True, null=True)
    github_url = models.CharField(max_length=2555, blank=True, null=True)

    def __str__(self):
        return f"{self.lastname} {self.name}"
    
    
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Modèle Projet
class Projet(models.Model):
    main_image = models.ImageField(upload_to='Projets/Main')
    title = models.CharField(max_length=2555)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='projets')
    utilisateurs = models.ManyToManyField(Utilisateur, related_name='projets')

    def __str__(self):
        return self.title
    
class Photo(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='Projets/Photos')

    def __str__(self):
        return f'Photo for {self.projet.title}'
    
class Video(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='Projets/Videos')

    def __str__(self):
        return f'Video for {self.projet.title}'
    

    
from django.db import models

class Post(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)

class Location(models.Model):
    location_id = models.IntegerField(primary_key=True)
    google_map_address = models.CharField(max_length=200)

class PostLocation(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Page(models.Model):
    content = models.TextField()
    image_url = models.URLField()
    like = models.IntegerField(default=0)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

from django.db import models

# Create your models here.
class Genre(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
      return self.name
  

class Game(models.Model):
   title = models.CharField(max_length=200)
   genre = models.ForeignKey('Genre', on_delete=models.CASCADE, related_name='games')  
   image = models.ImageField(upload_to='game_images/')
   description = models.TextField()

   def __str__(self):
       return self.title

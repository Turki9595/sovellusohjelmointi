from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class B_game(models.Model):#Board game class
    name = models.CharField(max_length= 40)#Pelin nimi
    description = models.TextField() #lyhyt pelin kuvaus
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name


class Review(models.Model):
    #A review on a book in question
    b_game = models.ForeignKey(B_game, on_delete = models.CASCADE)
    text = models.TextField()
    stars = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
     )
    date_added = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = 'reviews'
    def __str__(self):
      return f"{self.text[:50]}..."
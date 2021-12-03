from django.db import models

# Create your models here.
class B_game(models.Model):#Board game class
    description = models.CharField(max_length = 200)#lyhyt pelin kuvaus
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.description
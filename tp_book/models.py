from datetime import datetime

from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=150)
    desc = models.TextField()
    image = models.ImageField(upload_to='images',default='',null=True,blank=True)
    fav = models.BooleanField(default=False)
    # created_at = models.DateTimeField(default=datetime.now )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name+' - '+self.author

    def get_description(self):
        return self.desc[:60]


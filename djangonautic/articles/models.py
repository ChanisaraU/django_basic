from django.db import models

# Create your models here.
class articles(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    

    def __str__(self) :
        return self.title

    def cutbody(self) :
        return self.body[:20]+"..."    
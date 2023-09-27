from django.db import models

# Create your models here.
class User(models.Model):
    name= models.CharField()
    atualRank= models.CharField()
    highstRank= models.CharField()


class TopMaps(models.Model):
    topMaps= models.CharField(str)
    win= models.CharField(str)
    loss= models.CharField(str)


class TopAgents(models.Model):
    topAgents= models.CharField(str)
    win= models.CharField(str)
    loss= models.CharField(str)

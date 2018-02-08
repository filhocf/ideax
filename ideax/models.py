from django.db import models
from django.utils import timezone

"""
class Idea(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
"""

class Phase(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Criterion(models.Model):
    description = models.CharField(max_length=40)
    peso = models.IntegerField()

    def __str__(self):
        return self.description

class Evaluation_Item(models.Model):
    value = models.IntegerField(default=0)
    criterion = models.ForeignKey(Criterion,on_delete=models.PROTECT)

class Idea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    creation_date = models.DateTimeField('data criação')
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    phase = models.ForeignKey(Phase,on_delete=models.PROTECT)

    def count_likes(self):
        return self.popular_vote_set.filter(like=True).count()

class Vote(models.Model):
    evaluation_item = models.ForeignKey(Evaluation_Item,on_delete=models.PROTECT)
    value = models.IntegerField()
    voter = models.ForeignKey('auth.User',on_delete=models.PROTECT)
    idea = models.ForeignKey('Idea',on_delete=models.PROTECT)
    voting_date = models.DateTimeField('data da votação')

class Popular_Vote(models.Model):
    like = models.BooleanField()
    voter = models.ForeignKey('auth.User',on_delete=models.PROTECT)
    voting_date = models.DateTimeField()
    idea = models.ForeignKey('Idea',on_delete=models.PROTECT)

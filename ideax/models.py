from django.db import models
from django.utils import timezone
from enum import Enum

class Phase(Enum):
    GROW     = (1, 'Crescendo')
    RATE     = (2, 'Avaliando')
    ACT      = (3, 'Agindo')
    DONE     = (4, 'Feita')
    ARCHIVED = (5, 'Arquivada')

    def __init__(self, id, description):
        self.id = id
        self.description = description

    @classmethod
    def choices(cls):
        return tuple((x.id, x.description) for x in cls)

    @classmethod
    def get_phase_by_id(cls, id):
        for x in cls:
            if x.id == id:
                return x
        return None

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
    phase = models.PositiveSmallIntegerField(choices=Phase.choices())

    def count_popular_vote(self, like_boolean):
        return self.popular_vote_set.filter(like=like_boolean).count()
    def count_dislikes(self):
        return self.count_popular_vote(False)
    def count_likes(self):
        return self.count_popular_vote(True)


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

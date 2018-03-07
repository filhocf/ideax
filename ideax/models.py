from django.db import models
from django.utils import timezone
from enum import Enum

class Phase(Enum):
    GROW     = (1, 'Discussão', 'discussao', 'comments')
    RATE     = (2, 'Avaliação', 'avaliando','star')
    APROVED  = (3, 'Aprovação', 'aprovacao','star')
    ACT      = (4, 'Desenvolvimento', 'desenvolvimento','tasks')
    DONE     = (5, 'Feita', 'feita', 'check')
    ARCHIVED = (6, 'Arquivada', 'arquivada', 'archive')
    PAUSED   = (7, 'Pausada', 'pausada', 'paused')


    def __init__(self, id, description, css_class, icon_class):
        self.id = id
        self.description = description
        self.css_class =  css_class
        self.css_icon_class = icon_class;


    @classmethod
    def choices(cls):
        return tuple((x.id, x.description) for x in cls)

    @classmethod
    def get_phase_by_id(cls, id):
        for temp in cls:
            if temp.id == id:
                return temp
        return None

    @classmethod
    def get_css_class(cls, id):
        return cls.get_phase_by_id(id)

class Phase_History(models.Model):
    current_phase = models.PositiveSmallIntegerField()
    previous_phase = models.PositiveSmallIntegerField()
    date_change = models.DateTimeField('data da mudança')
    idea = models.ForeignKey('Idea',on_delete=models.DO_NOTHING)
    author = models.ForeignKey('auth.User',on_delete=models.DO_NOTHING)
    current = models.BooleanField()

class Criterion(models.Model):
    description = models.CharField(max_length=40)
    peso = models.IntegerField()

    def __str__(self):
        return self.description

class Evaluation_Item(models.Model):
    value = models.IntegerField(default=0)
    criterion = models.ForeignKey(Criterion,on_delete=models.PROTECT)

class Category(models.Model):
    description = models.CharField(max_length=200)
    key_word = models.CharField(max_length=50)

    def __str__(self):
        return self.description

class Idea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    creation_date = models.DateTimeField('data criação')
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    category = models.ForeignKey('Category', models.SET_NULL,null=True)
    discarded = models.BooleanField(default=False)

    def count_popular_vote(self, like_boolean):
        return self.popular_vote_set.filter(like=like_boolean).count()
    def count_dislikes(self):
        return self.count_popular_vote(False)
    def count_likes(self):
        return self.count_popular_vote(True)
    def get_current_phase_history(self):
        return self.phase_history_set.get(current=True)
    def get_current_phase(self):
        return Phase.get_phase_by_id(self.phase_history_set.get(current=True).current_phase)

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

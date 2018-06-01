from django.contrib.syndication.views import Feed
from django.utils.translation import ugettext_lazy as _
from ideax.models import *

class Comment_Feed(Feed):
    title = "ideax - Comentários"
    link = "/rss"
    description = "Compartilhando ideias"

    def items(self):
        return Comment.objects.all().order_by('-date')[:10]

    def item_title(self, item):
        return "Ideia: " + item.idea.title

    def item_description(self, item):
        comment = (item.raw_comment[:200] + ' ...') if len(item.raw_comment) > 75 else item.raw_comment
        comment += '</br></br>'+str(_('Comment by: '))+'<strong> '+' '+ item.author.user.username +'</strong>'
        return comment

    def item_link(self, item):
        return  "/idea/"+ str(item.idea.id) + "/#" + str(item.id)


class New_Idea_Feed(Feed):
    title = "ideax - Novas Ideias"
    link = "/rss"
    description = "Compartilhando ideias"

    def items(self):
        return Idea.objects.all().order_by('-creation_date')[:10]

    def item_title(self, item):
        return "Ideia: " + item.title

    def item_description(self, item):
        return item.summary

    def item_link(self, item):
        return  "/idea/"+str(item.id)

       




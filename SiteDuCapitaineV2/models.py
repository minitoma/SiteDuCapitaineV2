from django.contrib.syndication.views import Feed
from django.urls import reverse
from projet.models import Projet

class LatestEntriesFeed(Feed):
    title = "Site du Capitaine Minitoma"
    link = "/"
    description = "Dernier projet"

    def items(self):
        return Projet.objects.order_by('-published_date')[:1]

    def item_title(self, item):
        return item.titre

    def item_description(self, item):
        return item.description

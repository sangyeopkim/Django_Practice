from django.views.generic import ListView, DetailView

from bookmark.models import Bookmark


# ListView (Generic View)
class BookmarkLV(ListView):
    model = Bookmark


# DetailView (Generic View)
class BookmarkDV(DetailView):
    model = Bookmark

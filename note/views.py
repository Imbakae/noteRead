from django.shortcuts import render, get_object_or_404

# Create your views here.
from note.models import BlogArticles


def note_article(request, article_id):
    article = get_object_or_404(BlogArticles, id=article_id)
    pub = article.publish
    return render(request, "note_page/base.html", {"article": article, "publish": pub})


def note_title(request):
    return render(request, "note_page/base.html")

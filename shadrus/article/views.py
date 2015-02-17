from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from article.forms import CommentForm
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from django.contrib import auth
from django.contrib.auth.models import User
from datetime import datetime

# Create your views here.

def basic_one(request):
    view = "basic_one"
    html = "<html><body><h1>Hello %s</h1></body></html>" % view
    return HttpResponse(html)

def template_two(request):
    view = "template_two"
    t = get_template('myview.html')
    html = t.render(Context({'name':view}))
    return HttpResponse(html)

def template_three_simple(request):
    view = "template_three_simple"
    return render_to_response('myview.html', {'name': view})

def articles(request, page_number=1):
    all_articles = Article.objects.all().order_by('-article_data')
    current_page = Paginator(all_articles, 3)
    return render_to_response('articles.html', {'articles': current_page.page(page_number), 'username':auth.get_user(request).username})

# def article(request, article_id=1):
#     print "Hello"
#     return render_to_response('article.html', {'article': Article.objects.get(id=article_id),
#                                                'comments': Comments.objects.filter(comments_article_id=article_id)})


def article(request, article_id=1):
    comment_form=CommentForm
    args={}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)

def addlike(request, article_id):
    back_url = request.META['HTTP_REFERER']
    try:
        if article_id in request.COOKIES:
            redirect('/')
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect(back_url)
            response.set_cookie(article_id, "test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect(back_url)

def addcomment(request, article_id):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            comment.comments_date = datetime.now()
            comment.comments_from = User.objects.get(username = auth.get_user(request).username)
            print comment.comments_date
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/articles/get/%s' % article_id)

























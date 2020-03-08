from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

# Create your views here.
from myblog.models import Post,Category,Tag
import markdown
from django.core.paginator import Paginator


def index(request,pindex):
    posts = Post.objects.order_by('-created_time')
    categorys = Category.objects.all()

    # divide to pages
    paginator = Paginator(posts, 4)

    # get page-1
    if (pindex == ''):
        page = paginator.page(1)
    else:
        page = paginator.page(int(pindex))

    sum = paginator.num_pages


    return render(request,'myblog/index.html',{'page':page,'categorys':categorys,'sum':sum})

def detail(request,id):
    post = get_object_or_404(Post,id=id)
    post.content = markdown.markdown(post.content,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])
    categorys = Category.objects.all()
    tags = Tag.objects.all()
    recent_posts = Post.objects.all().order_by('-created_time')[0:3]
    # problem
    dates = Post.objects.dates('date', 'month', order='DESC')

    return render(request,'myblog/detail.html',{'post':post,'categorys':categorys,'recent_posts':recent_posts,'dates':dates})

def category(request,id,pindex):# /5/1
    posts = Post.objects.filter(category_id=id).order_by('-created_time')
    categorys = Category.objects.all()
    current_category = Category.objects.filter(id=id)[0:1].values()[0]
    current_category_name = current_category['name']
    current_id = current_category['id']

    # divide to pages
    paginator = Paginator(posts, 4)

    # get page-1
    if (pindex == ''):
        page = paginator.page(1)
    else:
        page = paginator.page(int(pindex))
    sum = paginator.num_pages

    num_of_posts = len(posts)

    return render(request,'myblog/category.html',{'page':page,'categorys':categorys,'current_category_name':current_category_name,'current_id':current_id,'sum':sum,'num_of_posts':num_of_posts})

def archives(request,year,month,pindex):
    posts = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    categorys = Category.objects.all()

    # divide to pages
    paginator = Paginator(posts, 4)

    # get page-1
    if (pindex == ''):
        page = paginator.page(1)
    else:
        page = paginator.page(int(pindex))
    sum = paginator.num_pages
    num_of_posts = len(posts)
    return render(request,'myblog/archives.html',{'page':page,'year':year,'month':month,'categorys':categorys,'sum':sum,'num_of_posts':num_of_posts})
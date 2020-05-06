from django.shortcuts import render
from django.http import HttpResponse
# from .models import Blogpost
# from fitness_blog.models import *
from .models import leg
from .models import chest1
from .models import back
from .models import fullbody1
from .models import bicep1
from .models import tricep1
from .models import shoulder1
from .models import forearm1
from .models import abs1
from .models import chest1
from .models import leg
from .models import shoulder1
from .models import tricep1
from .models import bicep1
from .models import forearm1
from .models import fullbody1
from .models import Blogpost
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
# Create your views here.




def home(request):
    # post1 = reversed(Blogpost.objects.all())
    # print(post1)
    # post1.reverse()
    # post1 = Blogpost.objects.all()
    post1 = Blogpost.objects.order_by('-post_id').all()
    print(type((post1.reverse())))

    paginator = Paginator(post1, 100)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1

    try:
        posts = paginator.page(page)
    except():
        posts = paginator.page(paginator,3)

    # print(post1)
    return render(request,"blog/index.html", {'post':posts})


def search(request):
    query = request.GET.get('search')
    all_blogs= Blogpost.objects.all()
    searched_blogs=[]
    for item in all_blogs:
        word= item.title.lower().split()

        if query in word:
            searched_blogs.append(item)
            print(item.title, "this is filtered.........Mubarak button is working....!!!!!!!!!!!")
    for t in searched_blogs:
        print(t, "from the list")

    print(query)
    # for items in all_blogs:
        # split_items = items.split(" ")
    # print(query, a)
    if len(searched_blogs) != 0:

        return render(request, "blog/search.html", {'post': searched_blogs, "length":len(searched_blogs)})
    else:
        print("it is reaching here")
        return render(request, "blog/not_found.html", {"length":len(searched_blogs)})



def blog_detail(request, id):
    # Blog.objects.filter(pk__in=[1, 4, 7])
    blog = Blogpost.objects.filter(post_id=id)[0]
    return render(request,"blog/blog_detail.html", {"blog": blog})

def chest(request):
    post2 = chest1.objects.all()[0]
    # print(post2.post_id)
    return render(request, "blog/chests.html", {'post': post2})

def legs(request):
    post = leg.objects.all()[0]
    print(post)
    return render(request, "blog/legs.html", {'post': post})


def back1(request):
    post = back.objects.all()[0]
    print(post)
    return render(request, "blog/legs.html", {'post': post})


def fullbody(request):
    post = fullbody1.objects.all()[0]
    print(post)
    return render(request, "blog/full-body.html", {'post': post})


def bicep(request):
    post = bicep1.objects.all()[0]
    print(post)
    return render(request, "blog/bicep.html", {'post': post})


def tricep(request):
    post = tricep1.objects.all()[0]
    print(post)
    return render(request, "blog/bicep.html", {'post': post})


def shoulder(request):
    post = shoulder1.objects.all()[0]
    print(post)
    return render(request, "blog/shoulder.html", {'post': post})

def forearm(request):
    post = forearm1.objects.all()[0]
    print(post)
    return render(request, "blog/forearm.html", {'post': post})

def abs(request):
    post = abs1.objects.all()[0]
    print(post)
    return render(request, "blog/abs.html", {'post': post})





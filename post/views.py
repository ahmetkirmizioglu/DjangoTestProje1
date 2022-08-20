from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect,redirect, Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.utils.text import slugify
from django.db.models import Q

# Create your views here.
def home_view(request):
    return HttpResponse('<b>Hoşgeldiniz</b>')

def post_index(request):
    posts = Post.objects.all()
    query = request.GET.get('q')
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()

    return render(request,'post/index.html', {'posts':posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post':post,
    }
    return render(request,'post/detail.html',context)

def post_create(request):


    if not request.user.is_authenticated:
        raise Http404


    form = PostForm()
    context = {
        'form' : form,
    }

    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Kayıt Başarılı.',extra_tags='basarili')
            return HttpResponseRedirect(post.get_absolute_url())
    else:

        form = PostForm()

        #form = PostForm(request.POST or None)
        #if form.is_valid():
        #    form.save()

    context = {
            'form' : form,
    }




   # if request.method == "POST":
   #     print(request.POST)

    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # Post.objects.create(title=title, content=content)
    return render(request,'post/form.html',context)




def post_update(request, id):

    if not request.user.is_authenticated:
        raise Http404

    post = get_object_or_404(Post, id=id)
    if request.user.id != post.user_id:
        raise Http404

    #post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
       form.save()
       messages.success(request, 'Güncelleme Başarılı.',extra_tags='basarili')
       return HttpResponseRedirect(post.get_absolute_url())
    context = {
            'form' : form,
    }
    return render(request, 'post/form.html', context)




def post_delete(request, id):

    if not request.user.is_authenticated:
        raise Http404


    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post:index')



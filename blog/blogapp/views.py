from django.shortcuts import render,get_object_or_404

# Create your views here.
from blogapp.models import Blog
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blogapp.form import CommentForm
from taggit.models import Tag


def Blog_list_view(request,tag_slug=None):
    Blog_list = Blog.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        Blog_list=Blog_list.filter(tags__in=[tag])
    paginator = Paginator(Blog_list,8)
    page_number = request.GET.get('page')
    try:
        Blog_list = paginator.page(page_number)
    except PageNotAnInteger:
        Blog_list = paginator.page(1)
    except EmptyPage:
        Blog_list = paginator.page(paginator.num_pages)
    return render(request,'blog/home.html',{'Blog_list':Blog_list,'tag':tag})


def Blog_Details_view(request,post):
    post=get_object_or_404(Blog, slug=post,
                                    status='published',)
    comments = post.comments.filter(active=True)
    csubmit = False
    if request.method == 'POST':
        form= CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit = True
    else:
        form = CommentForm()

    return render(request,'blog/blog_detail.html',{'post':post,'form':form,'csubmit':csubmit,'comments':comments})


def Tag_list_view(request):
    Tag_list=Tag.objects.all()
    return render(request,'blog/home.html',{'Tag_list':Tag_list})
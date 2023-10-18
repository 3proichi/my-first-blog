from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('deadline')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        #フォーム内のデータが正常であれば
        #（すべての必須フィールドが設定され、不正な値が送信されないこと）
        if form.is_valid():
            #フォームを保存
            #commit=False は Post モデルをまだ保存しないという意味
            post = form.save(commit=False)
            #authorを追加
            post.author = request.user
            post.published_date = timezone.now()
            #作成者を追加しつつフォームの変更を保存
            post.save()
            #Post＿detail
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_start(request):
    start = Post.objects.filter(published_date__lte=timezone.now()).order_by('deadline')
    return render(request, 'blog/start.html',{'start':start})
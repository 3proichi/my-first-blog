from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import ScheduleForm
from .forms import NotDesideScheduleForm
from django.shortcuts import redirect



# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('deadline')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_nyuuryoku(request):
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

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def anotherpost(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('choice')
    return render(request, 'blog/post_list.html', {'posts': posts})


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

def souziki_post_new(request):
    if request.method == "POST":
        form = NotDesideScheduleForm(request.POST)
        
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
        default_data = {'title':"掃除機",'text':"の部屋の掃除機をかける"}
        form = NotDesideScheduleForm(default_data)
    return render(request, 'blog/post_edit.html', {'form': form})

def zyugyou_post_new(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        
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
        default_data = {'text':"授業"}
        form = ScheduleForm(default_data)
    return render(request, 'blog/post_edit.html', {'form': form})

def baito_post_new(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        
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
        default_data = {'title':"アルバイト",'text':"アルバイト"}
        form = ScheduleForm(default_data)
    return render(request, 'blog/post_edit.html', {'form': form})

def yotei_post_new(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        
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
        form = ScheduleForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post2 = Post.objects.filter(published_date__lte=timezone.now()).order_by('deadline')
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
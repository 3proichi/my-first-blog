from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import ScheduleForm
from django.shortcuts import redirect
import datetime



# Create your views here.
def post_list(request):
    posts = Post.objects.filter(deadline__isnull=False).order_by('deadline')
    today = timezone.now()
    context={'posts':posts,'today':today}
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form1 = PostForm(request.POST)
        #フォーム内のデータが正常であれば
        #（すべての必須フィールドが設定され、不正な値が送信されないこと）
        if form1.is_valid():
            #フォームを保存
            #commit=False は Post モデルをまだ保存しないという意味
            post = form1.save(commit=False)
            #authorを追加
            post.author = request.user
            post.published_date = timezone.now()
            #作成者を追加しつつフォームの変更を保存
            post.save()
            #Post＿detail
            return redirect('post_detail', pk=post.pk)
    else:
        form1 = PostForm()
    return render(request, 'blog/post_edit.html', {'form1': form1})

def souziki_post_new(request):
    if request.method == "POST":
        form2 = PostForm(request.POST)
        
        #フォーム内のデータが正常であれば
        #（すべての必須フィールドが設定され、不正な値が送信されないこと）
        if form2.is_valid():
            #フォームを保存
            #commit=False は Post モデルをまだ保存しないという意味
            post = form2.save(commit=False)
            #authorを追加
            post.author = request.user
            post.published_date = timezone.now()
            #作成者を追加しつつフォームの変更を保存
            post.save()
            #Post＿detail
            return redirect('post_detail', pk=post.pk)
    else:
        default_data = {'title':"掃除機",'text':"の部屋の掃除機をかける"}
        form2 = PostForm(default_data)
    return render(request, 'blog/post_edit.html', {'form2': form2})

def zyugyou_post_new(request):
    if request.method == "POST":
        form3 = ScheduleForm(request.POST)
        
        #フォーム内のデータが正常であれば
        #（すべての必須フィールドが設定され、不正な値が送信されないこと）
        if form3.is_valid():
            #フォームを保存
            #commit=False は Post モデルをまだ保存しないという意味
            post = form3.save(commit=False)
            #authorを追加
            post.author = request.user
            post.published_date = timezone.now()
            #作成者を追加しつつフォームの変更を保存
            post.save()
            #Post＿detail
            return redirect('post_detail', pk=post.pk)
    else:
        default_data = {'text':"授業"}
        form3 = ScheduleForm(default_data)
    return render(request, 'blog/post_edit.html', {'form3': form3})

def baito_post_new(request):
    if request.method == "POST":
        form4 = ScheduleForm(request.POST)
        
        #フォーム内のデータが正常であれば
        #（すべての必須フィールドが設定され、不正な値が送信されないこと）
        if form4.is_valid():
            #フォームを保存
            #commit=False は Post モデルをまだ保存しないという意味
            post = form4.save(commit=False)
            #authorを追加
            post.author = request.user
            post.published_date = timezone.now()
            #作成者を追加しつつフォームの変更を保存
            post.save()
            #Post＿detail
            return redirect('post_detail', pk=post.pk)
    else:
        default_data = {'title':"アルバイト",'text':"アルバイト"}
        form4 = ScheduleForm(default_data)
    return render(request, 'blog/post_edit.html', {'form4': form4})

def kazi_post_new(request):
    if request.method == "POST":
        form6 = PostForm(request.POST)
        
        #フォーム内のデータが正常であれば
        #（すべての必須フィールドが設定され、不正な値が送信されないこと）
        if form6.is_valid():
            #フォームを保存
            #commit=False は Post モデルをまだ保存しないという意味
            post = form6.save(commit=False)
            #authorを追加
            post.author = request.user
            post.published_date = timezone.now()
            #作成者を追加しつつフォームの変更を保存
            post.save()
            #Post＿detail
            return redirect('post_detail', pk=post.pk)
    else:
        form6 = PostForm()
    return render(request, 'blog/post_edit.html', {'form6': form6})

def yotei_post_new(request):
    if request.method == "POST":
        form5 = ScheduleForm(request.POST)
        
        #フォーム内のデータが正常であれば
        #（すべての必須フィールドが設定され、不正な値が送信されないこと）
        if form5.is_valid():
            #フォームを保存
            #commit=False は Post モデルをまだ保存しないという意味
            post = form5.save(commit=False)
            #authorを追加
            post.author = request.user
            post.published_date = timezone.now()
            #作成者を追加しつつフォームの変更を保存
            post.save()
            #Post＿detail
            return redirect('post_detail', pk=post.pk)
    else:
        form5 = ScheduleForm()
    return render(request, 'blog/post_edit.html', {'form5': form5})

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

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    posts = Post.objects.filter(deadline__isnull=False).order_by('deadline')
    today = timezone.now()
    context={'posts':posts,'today':today}
    return render(request, 'blog/post_list.html', context)

def post_start(request):
    start = Post.objects.filter(published_date__lte=timezone.now()).order_by('deadline')
    return render(request, 'blog/start.html',{'start':start})
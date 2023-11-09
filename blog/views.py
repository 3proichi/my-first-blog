from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import ScheduleForm
from django.shortcuts import redirect
import math

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(deadline__isnull=False).order_by('deadline')
    posts2 = Post.objects.filter(published_date__lte=timezone.now()).order_by('start_data')
    now = timezone.localtime(timezone.now())
    today_start = now-timezone.timedelta(hours=now.hour,minutes=now.minute,seconds=now.second,microseconds=now.microsecond)
    today_finish =  timezone.localtime(today_start)+timezone.timedelta(hours=23,minutes=59)
    context={'posts':posts,'today':now,'posts2':posts2,'today_s':today_start,'today_f':today_finish}
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
            post.save()
            print(post.deadline)
            now = timezone.localtime(timezone.now())
            
            #締め切りまでの日数計算
            limit = timezone.localtime(post.deadline) - now
            finish = False
            #締切の日数分ループ
            for l in range(0,limit.days):
                #探す日
                if finish:
                    break
                else:
                    searchday = now - timezone.timedelta(days=-l,hours=now.hour,minutes=now.minute,seconds=now.second,microseconds=now.microsecond)
                    posts = Post.objects.filter(start_data__date=searchday.date())

                    zikan = [False] * 24  # 24要素すべてをFalseで初期化
                    zikan[0]=True  # 24要素すべてをFalseで初期化
                    zikan[1]=True  # 24要素すべてをFalseで初期化
                    zikan[2]=True  # 24要素すべてをFalseで初期化
                    zikan[3]=True  # 24要素すべてをFalseで初期化
                    zikan[4]=True  # 24要素すべてをFalseで初期化
                    zikan[5]=True  # 24要素すべてをFalseで初期化
                    zikan[6]=True  # 24要素すべてをFalseで初期化
                    zikan[7]=True  # 24要素すべてをFalseで初期化
                    zikan[8]=True  # 24要素すべてをFalseで初期化
                    zikan[22]=True  # 24要素すべてをFalseで初期化
                    zikan[23]=True  # 24要素すべてをFalseで初期化


                    for post1 in posts:
                        s = timezone.localtime(post1.start_data)
                        f = timezone.localtime(post1.finish_data)
                        hours = (f-s).seconds/3600
                        for i in range(0,math.ceil(hours)):
                            zikan[i+s.hour] = True
                    
                    num = 0
                    min = 0
                    min = post.spendtime*60
                    if post.spendtime < 1:
                        for index in range(0,len(zikan)-1):
                            if zikan[index] == False:
                                post.start_data = searchday + timezone.timedelta(hours=index)
                                post.finish_data = timezone.localtime(post.start_data) + timezone.timedelta(minutes=min)
                                finish = True
                                break
                    else:
                        for index in range(0,len(zikan)-1):
                            if zikan[index] == False:
                                num += 1
                                if num >= post.spendtime:
                                    post.start_data = searchday + timezone.timedelta(hours=(index - (num-1)))
                                    post.finish_data = timezone.localtime(post.start_data) + timezone.timedelta(minutes=min)
                                    finish = True
                                    break
                            else:
                                num = 0


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

            now = timezone.localtime(timezone.now())
            #締め切りまでの日数計算
            limit = timezone.localtime(post.deadline) - now
            finish = False
            #締切の日数分ループ
            for l in range(0,limit.days):
                #探す日
                if finish:
                    break
                else:
                    searchday = now - timezone.timedelta(days=-l,hours=now.hour,minutes=now.minute,seconds=now.second,microseconds=now.microsecond)
                    posts = Post.objects.filter(start_data__date=searchday.date())

                    zikan = [False] * 24  # 24要素すべてをFalseで初期化
                    zikan[0]=True  # 24要素すべてをFalseで初期化
                    zikan[1]=True  # 24要素すべてをFalseで初期化
                    zikan[2]=True  # 24要素すべてをFalseで初期化
                    zikan[3]=True  # 24要素すべてをFalseで初期化
                    zikan[4]=True  # 24要素すべてをFalseで初期化
                    zikan[5]=True  # 24要素すべてをFalseで初期化
                    zikan[6]=True  # 24要素すべてをFalseで初期化
                    zikan[7]=True  # 24要素すべてをFalseで初期化
                    zikan[8]=True  # 24要素すべてをFalseで初期化
                    zikan[22]=True  # 24要素すべてをFalseで初期化
                    zikan[23]=True  # 24要素すべてをFalseで初期化


                    for post1 in posts:
                        s = timezone.localtime(post1.start_data)
                        f = timezone.localtime(post1.finish_data)
                        hours = (f-s).seconds/3600
                        for i in range(0,math.ceil(hours)):
                            zikan[i+s.hour] = True
                    
                    num = 0
                    min = 0
                    min = post.spendtime*60
                    if post.spendtime < 1:
                        for index in range(0,len(zikan)-1):
                            if zikan[index] == False:
                                post.start_data = searchday + timezone.timedelta(hours=index)
                                post.finish_data = timezone.localtime(post.start_data) + timezone.timedelta(minutes=min)
                                finish = True
                                break
                    else:
                        for index in range(0,len(zikan)-1):
                            if zikan[index] == False:
                                num += 1
                                if num >= post.spendtime:
                                    post.start_data = searchday + timezone.timedelta(hours=(index - (num-1)))
                                    post.finish_data = timezone.localtime(post.start_data) + timezone.timedelta(minutes=min)
                                    finish = True
                                    break
                            else:
                                num = 0
            #作成者を追加しつつフォームの変更を保存
            post.save()
            #Post＿detail
            return redirect('post_detail', pk=post.pk)
    else:
        default_data = {'title':"掃除機",'text':"の部屋の掃除機をかける"}
        form2 = PostForm(default_data)
    return render(request, 'blog/post_edit.html', {'form2': form2})

def sentaku_post_new(request):
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

            now = timezone.localtime(timezone.now())
            #締め切りまでの日数計算
            limit = timezone.localtime(post.deadline) - now
            finish = False
            #締切の日数分ループ
            for l in range(0,limit.days):
                #探す日
                if finish:
                    break
                else:
                    searchday = now - timezone.timedelta(days=-l,hours=now.hour,minutes=now.minute,seconds=now.second,microseconds=now.microsecond)
                    posts = Post.objects.filter(start_data__date=searchday.date())

                    zikan = [False] * 24  # 24要素すべてをFalseで初期化
                    zikan[0]=True  # 24要素すべてをFalseで初期化
                    zikan[1]=True  # 24要素すべてをFalseで初期化
                    zikan[2]=True  # 24要素すべてをFalseで初期化
                    zikan[3]=True  # 24要素すべてをFalseで初期化
                    zikan[4]=True  # 24要素すべてをFalseで初期化
                    zikan[5]=True  # 24要素すべてをFalseで初期化
                    zikan[6]=True  # 24要素すべてをFalseで初期化
                    zikan[7]=True  # 24要素すべてをFalseで初期化
                    zikan[8]=True  # 24要素すべてをFalseで初期化
                    zikan[22]=True  # 24要素すべてをFalseで初期化
                    zikan[23]=True  # 24要素すべてをFalseで初期化


                    for post1 in posts:
                        s = timezone.localtime(post1.start_data)
                        f = timezone.localtime(post1.finish_data)
                        hours = (f-s).seconds/3600
                        for i in range(0,math.ceil(hours)):
                            zikan[i+s.hour] = True
                    
                    num = 0
                    min = 0
                    min = post.spendtime*60
                    if post.spendtime < 1:
                        for index in range(0,len(zikan)-1):
                            if zikan[index] == False:
                                post.start_data = searchday + timezone.timedelta(hours=index)
                                post.finish_data = timezone.localtime(post.start_data) + timezone.timedelta(minutes=min)
                                finish = True
                                break
                    else:
                        for index in range(0,len(zikan)-1):
                            if zikan[index] == False:
                                num += 1
                                if num >= post.spendtime:
                                    post.start_data = searchday + timezone.timedelta(hours=(index - (num-1)))
                                    post.finish_data = timezone.localtime(post.start_data) + timezone.timedelta(minutes=min)
                                    finish = True
                                    break
                            else:
                                num = 0
            #作成者を追加しつつフォームの変更を保存
            post.save()
            #Post＿detail
            return redirect('post_detail', pk=post.pk)
    else:
        default_data = {'title':"洗濯",'text':"洗濯機回す"}
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

            now = timezone.localtime(timezone.now())
            #締め切りまでの日数計算
            limit = timezone.localtime(post.deadline) - now
            finish = False
            #締切の日数分ループ
            for l in range(0,limit.days):
                #探す日
                if finish:
                    break
                else:
                    searchday = now - timezone.timedelta(days=-l,hours=now.hour,minutes=now.minute,seconds=now.second,microseconds=now.microsecond)
                    posts = Post.objects.filter(start_data__date=searchday.date())

                    zikan = [False] * 24  # 24要素すべてをFalseで初期化
                    zikan[0]=True  # 24要素すべてをFalseで初期化
                    zikan[1]=True  # 24要素すべてをFalseで初期化
                    zikan[2]=True  # 24要素すべてをFalseで初期化
                    zikan[3]=True  # 24要素すべてをFalseで初期化
                    zikan[4]=True  # 24要素すべてをFalseで初期化
                    zikan[5]=True  # 24要素すべてをFalseで初期化
                    zikan[6]=True  # 24要素すべてをFalseで初期化
                    zikan[7]=True  # 24要素すべてをFalseで初期化
                    zikan[8]=True  # 24要素すべてをFalseで初期化
                    zikan[22]=True  # 24要素すべてをFalseで初期化
                    zikan[23]=True  # 24要素すべてをFalseで初期化


                    for post1 in posts:
                        s = timezone.localtime(post1.start_data)
                        f = timezone.localtime(post1.finish_data)
                        hours = (f-s).seconds/3600
                        for i in range(0,math.ceil(hours)):
                            zikan[i+s.hour] = True
                    
                    num = 0
                    min = 0
                    min = post.spendtime*60
                    if post.spendtime < 1:
                        for index in range(0,len(zikan)-1):
                            if zikan[index] == False:
                                post.start_data = searchday + timezone.timedelta(hours=index)
                                post.finish_data = timezone.localtime(post.start_data) + timezone.timedelta(minutes=min)
                                finish = True
                                break
                    else:
                        for index in range(0,len(zikan)-1):
                            if zikan[index] == False:
                                num += 1
                                if num >= post.spendtime:
                                    post.start_data = searchday + timezone.timedelta(hours=(index - (num-1)))
                                    post.finish_data = timezone.localtime(post.start_data) + timezone.timedelta(minutes=min)
                                    finish = True
                                    break
                            else:
                                num = 0
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
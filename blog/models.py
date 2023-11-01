from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    CHOICES = (('3','!!!'),('2','!!'),('1','!'))
    choice = models.CharField(verbose_name="優先順位は？",max_length=50,choices = CHOICES,blank=True)

    #PostForm(タスク系の入力)に使っている
    title = models.CharField(verbose_name="どんなタスク？",blank=False, null=False, max_length=10, default=" ")
    text = models.TextField(verbose_name="どんな内容？")
    deadline = models.DateTimeField(verbose_name="いつまでにやらないといけない？", blank=True, null=True)

    #ScheduleForm(やる時間決まっている予定の入力)に使っている
    start_data = models.DateTimeField(verbose_name="いつから？", blank=True, null=True)
    finish_data = models.DateTimeField(verbose_name="いつまで？", blank=True, null=True)
    
    #NotDesideScheduleForm(やる時間決まっていない予定の入力)に使っている
    aboutdeadline  = models.DateField(verbose_name="いつまでにやらないといけない？", blank=True, null=True)
    spendtime = models.FloatField(verbose_name="何時間くらいかかる？", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
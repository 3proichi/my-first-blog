#Djangoのformsをインポート
from django import forms
#Postモデルインポート
from .models import Post

#PostFormという名前のフォームはModelFormの一種であるという宣言
#タスク系の入力+やる時間決まっていない予定フォーム
class PostForm(forms.ModelForm):

    class Meta:
        #Djangoにフォームを作るときにどのようなモデルを使うか宣言
        #models.pyで作ったモデルで選ぶ
        model = Post
        #フォームのフィールドに何を置くか
        fields = ('title','text','deadline','spendtime','choice')
        widgets = {
            'deadline': forms.NumberInput(attrs={
                "type": "datetime-local"
            })
            ,'spendtime': forms.NumberInput(attrs={'min':0,'step': "0.1"})
        }

#やる時間決まっている予定の入力フォーム
class ScheduleForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text','start_data','finish_data')
        widgets = {
            'start_data': forms.NumberInput(attrs={
                "type": "datetime-local"})
            ,'finish_data': forms.NumberInput(attrs={
                "type": "datetime-local"
            })
        }
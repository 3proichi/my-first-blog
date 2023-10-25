#Djangoのformsをインポート
from django import forms
#Postモデルインポート
from .models import Post

#PostFormという名前のフォームはModelFormの一種であるという宣言
#タスク系の入力フォーム
class PostForm(forms.ModelForm):

    class Meta:
        #Djangoにフォームを作るときにどのようなモデルを使うか宣言
        #models.pyで作ったモデルで選ぶ
        model = Post
        #フォームのフィールドに何を置くか
        fields = ('title','text','deadline')
        widgets = {
            'deadline': forms.NumberInput(attrs={
                "type": "datetime-local"
            })
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

#やる時間決まっていない予定の入力フォーム
class NotDesideScheduleForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text','aboutdeadline','spendtime','choice')
        widgets = {
            'aboutdeadline': forms.NumberInput(attrs={
                "type": "date"
            })
            ,'spendtime': forms.NumberInput(attrs={'min':0,'step': "0.1"})
        }
#Djangoのformsをインポート
from django import forms
#Postモデルインポート
from .models import Post

#PostFormという名前のフォームはModelFormの一種であるという宣言
class PostForm(forms.ModelForm):

    class Meta:
        #Djangoにフォームを作るときにどのようなモデルを使うか宣言
        #models.pyで作ったモデルで選ぶ
        model = Post
        #フォームのフィールドに何を置くか
        fields = ('task','text','deadline','task')
        widgets = {
            'deadline': forms.NumberInput(attrs={
                "type": "date"
            })
        }
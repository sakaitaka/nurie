from django import forms


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='>> 写真ファイルを選択する',)


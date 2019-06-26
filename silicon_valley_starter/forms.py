from django import forms

class PostLimitForm(forms.Form):
    limit = forms.IntegerField(label='enter cache limit')

class GetStringForm(forms.Form):
    string_text = forms.CharField(label='enter a value to get the results for')



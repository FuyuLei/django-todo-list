from django.forms import ModelForm, Form, BooleanField

from .models import Todo


class TodoModelFrom(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['creator']


class DeleteConfirmForm(Form):
    check = BooleanField(label='你確定要刪除嗎?')
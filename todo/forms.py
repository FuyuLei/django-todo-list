from django.forms import ModelForm, Form, BooleanField

from .models import Todo


class TodoModelFrom(ModelForm):
    class Meta:
        model = Todo
        exclude = ['creator']

    def save(self, user, commit=True):
        todo = super(TodoModelFrom, self).save(commit=False)  # super().save(commit=False)
        todo.creator = user
        todo.save()

        self.save_m2m()

        return todo


class DeleteConfirmForm(Form):
    check = BooleanField(label='你確定要刪除嗎?')

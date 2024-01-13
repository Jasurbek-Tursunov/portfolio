from django.forms import ModelForm

from frontend.models import Message


class MessagesForm(ModelForm):

    class Meta:
        model = Message
        exclude = "avatar", "is_checked"

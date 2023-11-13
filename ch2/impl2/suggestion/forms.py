from django import forms
from suggestion.tasks import send_email_task, write_log


class SuggestionForm(forms.Form):
    name = forms.CharField(label="Your name")
    email = forms.EmailField(label="Email address")
    suggestion = forms.CharField(
        label="Your suggestion", widget=forms.Textarea(attrs={"rows": 7})
    )

    def send_email(self):
        send_email_task.delay(
            self.cleaned_data["name"], self.cleaned_data["email"], self.cleaned_data["suggestion"]
        )

    def write_log_message(self):
        write_log.delay(self.cleaned_data["suggestion"])

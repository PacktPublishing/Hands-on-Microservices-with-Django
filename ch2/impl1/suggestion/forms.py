from django import forms

from suggestion.producer import send_email_task_message


class SuggestionForm(forms.Form):
    name = forms.CharField(label="Your name")
    email = forms.EmailField(label="Email")
    suggestion = forms.CharField(
        label="Your suggestion", widget=forms.Textarea(attrs={"rows": 7})
    )

    def send_email(self):
        task_message = {
            "name": self.cleaned_data["name"],
            "email": self.cleaned_data["email"],
            "suggestion": self.cleaned_data["suggestion"]
        }
        send_email_task_message(task_message)

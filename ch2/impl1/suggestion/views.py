from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from suggestion.forms import SuggestionForm


class SuggestionFormView(FormView):
    template_name = "suggestion/suggestion.html"
    form_class = SuggestionForm
    success_url = "/success/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = "suggestion/success.html"

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import SubscriptionForm
from .producer import match_address_task_message


class SubscriptionFormView(FormView):
    template_name = "subscription/subscription.html"
    form_class = SubscriptionForm
    success_url = "/success/"

    def form_valid(self, form):
        task_message = {
            "name": form.cleaned_data["name"],
            "address": form.cleaned_data["address"],
            "postalcode": form.cleaned_data["postalcode"],
            "city": form.cleaned_data["city"],
            "country": form.cleaned_data["country"],
            "email": form.cleaned_data["email"]
        }
        match_address_task_message(task_message)

        # form.match_address()
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = "subscription/success.html"

import os

from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from dotenv import load_dotenv
from subscription.forms import SubscriptionForm
from subscription.tasks import match_address_task
from .models import Magazine

load_dotenv()

client_token = os.getenv("CLIENT_TOKEN")


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
            "email": form.cleaned_data["email"],
            "client_token": client_token
        }
        match_address_task.delay(task_message)

        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = "subscription/success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        magazines = cache.get("magazines")

        # magazines = Magazine.objects.all()
        context['magazines'] = magazines
        return context

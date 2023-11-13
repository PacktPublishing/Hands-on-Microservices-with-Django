from django.urls import path

from suggestion.views import SuggestionFormView, SuccessView

app_name = "feedback"

urlpatterns = [
    path("", SuggestionFormView.as_view(), name="feedback"),
    path("success/", SuccessView.as_view(), name="success"),
]

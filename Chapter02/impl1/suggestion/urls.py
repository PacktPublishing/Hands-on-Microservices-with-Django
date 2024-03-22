from django.urls import path

from suggestion.views import SuggestionFormView, SuccessView

app_name = "suggestion"

urlpatterns = [
    path("suggestion/", SuggestionFormView.as_view(), name="suggestion"),
    path("success/", SuccessView.as_view(), name="success"),
]

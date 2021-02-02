from django.urls import path
from .views import IndexView, AboutView, EveresView


urlpatterns = [
    path('', IndexView.as_view()),
    path('about/', AboutView.as_view()),
    path('everes/', EveresView.as_view()),
]

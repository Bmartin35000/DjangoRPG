from django.urls import path
from .views import CharacterView

urlpatterns = [
    path('', CharacterView.as_view()),
    path('<int:id>', CharacterView.as_view()),
]

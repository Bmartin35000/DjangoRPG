from django.urls import path
from .views import EnemyView

urlpatterns = [
    path('', EnemyView.as_view()),
    path('<int:id>', EnemyView.as_view()),
]

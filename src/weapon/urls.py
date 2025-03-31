from django.urls import path
from .views import WeaponView

urlpatterns = [
    path('', WeaponView.as_view()),
    path('<int:id>', WeaponView.as_view()),
]

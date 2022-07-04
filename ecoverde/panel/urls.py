from .views import userPanel, Compare, saves
from django.urls import path



urlpatterns = [
    path('user dashboard', userPanel, name='userPanel'),
    path('compare', Compare, name='compare'),
    path('saves', saves, name='saves')
]

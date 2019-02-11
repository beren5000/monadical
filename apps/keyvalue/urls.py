from django.urls import path
from django.views.generic import RedirectView

from apps.keyvalue.views import set_value, get_value, TicTacToe


urlpatterns = [
    path('', RedirectView.as_view(pattern_name='tic-tac-toe', permanent=False), name='home'),
    path('set/', set_value, name='set-value'),
    path('get/', get_value, name='get-value'),
    path('tic-tac-toe/', TicTacToe.as_view(), name='tic-tac-toe')
]

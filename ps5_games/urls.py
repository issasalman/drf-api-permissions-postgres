from django.urls import path
from .views import Ps5_gamesDetail,Ps5_gamesList

urlpatterns = [
    path('', Ps5_gamesList.as_view(), name = 'Ps5_gamesList_list'),
    path('<int:pk>/',Ps5_gamesDetail.as_view(), name = 'Ps5_gamesDetail_detail')

]
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index_url'),
    path('routes/', routes, name='routes_url'),
    path('outfit/', outfit, name='outfit_url'),

]
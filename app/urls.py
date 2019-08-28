from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index_url'),
    path('routes/', RoutesList.as_view(), name='routes_url'),
    path('outfit/<slug:slug>/', OutfitDetail.as_view(), name='outfit_url'),
    path('routes/<slug:slug>/', RoutesDetail.as_view(), name='detail_url'),
    path('rubrics/', RubricsView.as_view(), name='rubrics_url'),
    path('rubrics/<int:rubrics_id>/', RubricsDetail.as_view(), name='rubrics_detail_url'),


]
from django.urls import path
from bookmark.views import StockLV, StockDV, stockDB

app_name = 'bookmark'

urlpatterns = [
    path('', stockDB, name='stock_list'),
    path('detail', StockDV.stockDB_detail, name='stock_detail'),
]
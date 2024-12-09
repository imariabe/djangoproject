from django.urls import path
from.import views





urlpatterns = [
    path('', views.index, name='index'),  # 'index' is the name for this path
]







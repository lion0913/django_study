from django.urls import path

from . import views

urlpatterns = [
    # polls안의 path가 없다는 뜻
    path('', views.index, name='index'),
]
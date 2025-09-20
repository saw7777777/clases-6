from django.urls import path
from .views import postlistview

urlpatterns = [
    path('', postlistview.as_view(), name='post-list.html'),
]
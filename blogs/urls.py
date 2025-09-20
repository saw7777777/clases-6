from django.urls import path
from .views import postlistview, postdetailview

urlpatterns = [
    path('', postlistview.as_view(), name='post-list'),
    path('post/<int:pk>/', postdetailview.as_view(), name='post-detail'),
]
from django.urls import path
from .views import postlistview, postdetailview, postcreateview,postupdateview

urlpatterns = [
    path("", postlistview.as_view(), name="post-list"),
    path("post/<int:pk>/", postdetailview.as_view(), name="post-detail"),
    path("post/new/", postcreateview.as_view(), name="post-new"),
    path("post/<int:pk>/edit/", postupdateview.as_view(), name="post-edit"),
]

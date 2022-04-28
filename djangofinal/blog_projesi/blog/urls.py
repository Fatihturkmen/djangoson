from django.urls import path
from .views import (BlogListView ,
                    BlogDetailView,
                    BlogCreateView,
                    BlogUpdateView,
                     BlogDeleteView,
                    )
                   

urlpatterns=[
    path("post/<int:pk>/silme/", BlogDeleteView.as_view(), name="post_silme"),
    path("post/<int:pk>/edit", BlogUpdateView.as_view(), name="post_edit"),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path("post/yeni/", BlogCreateView.as_view(), name="post_yeni"),
    path('', BlogListView.as_view(), name='home'),
]
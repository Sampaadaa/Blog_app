from django.urls import path
from .views import BlogListView,BlogDetailView,AboutListView
from . import views



urlpatterns = [
    path('',views.HomeListView.as_view(),name="index"),  
    path('blog/',BlogListView.as_view(),name="blog"),
    path('blog/<int:page>',BlogListView.as_view(),name="blog-terminate"),
    path("blogs/<int:pk>/", BlogDetailView.as_view(),name="blog_detail"), 
    path('about/', AboutListView.as_view(),name="about"),  

    
]

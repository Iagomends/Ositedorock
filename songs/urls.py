from django.urls import path

from . import views

app_name = 'songs'
urlpatterns = [
    path('', views.SongListView.as_view(), name='index'),
    path('create/', views.SongCreateView.as_view(), name='create'),
    path('<int:pk>/', views.SongDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.SongUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.SongDeleteView.as_view(), name='delete'),
    path('<int:post_id>/comment/', views.create_comment, name='comment'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
]
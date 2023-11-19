from django.urls import path

from . import views

app_name = 'songs'
urlpatterns = [
    path('', views.post_list, name='index'),
    path('create/', views.post_create, name='create'),
    path('<int:pk>/', views.post_detail, name='detail'),
    path('update/<int:pk>/', views.post_update, name='update'),
    path('delete/<int:pk>/', views.post_delete, name='delete'),
    path('<int:post_id>/comment/', views.create_comment, name='comment'),
    path('category/<int:pk>', views.category_detail, name='category'),
    path('categories/', views.category_list, name='categories'),
]
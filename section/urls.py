from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("signup/", views.sign_up, name="signup"),
    path('list/', views.list_class, name='list'),
    path('new/', views.new_post, name='new_post'),
    path('post/<int:pk>/', views.post_view, name='post_view'),
    path("<username>/<int:post_id>/comment/", views.add_comment, name="add_comment"),
    path("<username>/<int:post_id>/apeal/", views.add_apeal, name="add_apeal"),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/edit/', views.update_profile, name='profile_edit'),
    path('<str:username>/delete/', views.delete_profile, name='profile_delete'),
    path('<str:username>/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('<int:post_id>/delete/', views.post_delete, name='post_delete'),
]
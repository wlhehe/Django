from django.urls import path
from blog import views as views
urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('post/create/', views.post_create_view, name='post_create_view'),
    path('post/<int:post_id>/update/', views.post_update_view, name='post_update_view'),
    path('post/<int:post_id>/delete/', views.post_delete_view, name='post_delete_view'),
    path('post/list/', views.post_list_view, name='post_list_view'),
    path('post/<int:post_id>/detail/', views.post_detail_view, name='post_detail_view'),
    path('post/<int:post_id>/update/', views.post_update_view, name='post_update_view'),
    path('post/<int:post_id>/delete/', views.post_delete_view, name='post_delete_view'),
    path('post/list/', views.post_list_view, name='post_list_view'),
]
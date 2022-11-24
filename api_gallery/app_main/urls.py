from django.urls import path
from .views import Login, Logout, RegisterView, GetCurrentUser, \
    UserAPI, UserDetailAPI, ImageAPI, ImageDetailAPI, \
    DeleteAll


urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    path('users/', UserAPI.as_view(), name='users_api_list'),
    path('users/<int:pk>/', UserDetailAPI.as_view(), name='users_api_detail'),

    path('images/', ImageAPI.as_view(), name='images_api_list'),
    path('images/<int:pk>/', ImageDetailAPI.as_view(), name='images_api_detail'),

    path('delete_all_images/', DeleteAll.as_view(), name='delete_all_images'),
    path('get_current_user/', GetCurrentUser.as_view(), name='get_current_user'),
]

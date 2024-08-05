from django.urls import path
from . import views
# importing views.py from the same folderd

# specifying the routes for the urlpatterns
urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('', views.home, name="home"),                              # 'root' url maps to the home view
    path('room/<str:pk>/', views.room, name="room"), 
    path('profile/<str:pk>/', views.userProfile, name="user-profile"), 
    path('update-user/', views.updateUser, name="update-user"),
    path('remove-avatar/', views.remove_avatar, name='remove-avatar'),

    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),

    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
]

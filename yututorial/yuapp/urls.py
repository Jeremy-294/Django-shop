from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create/', views.create, name='create'),
    path('register/', views.register, name='register'),
    path('loginpage/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('modifypwd/', views.modify_pwd, name='modifypwd'),

    path('updateorder/<str:pk>/', views.update_order, name='updateorder'),
    path('deleteorder/<str:pk>/', views.delete_order, name='deleteorder')
]

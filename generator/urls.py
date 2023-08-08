from django.urls import path


from . import views
urlpatterns = [
    path('', views.home, name='generator-home' ),
    path('easy/', views.easy_password, name='generator-easy_password'),
    path('medium/', views.medium_password, name='generator-medium_password'),
    path('hard/', views.hard_password, name='generator-hard_password'),
]
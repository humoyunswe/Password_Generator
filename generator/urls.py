from django.urls import path


from . import views
urlpatterns = [
    path('', views.home, name='generator-home' ),
    path('easy/', views.easy_password, name='easy_password'),
    path('medium/', views.medium_password, name='medium_password'),
    path('hard/', views.hard_password, name='hard_password'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.user_profile, name='user_profile'),
    path('accounts/signup/', views.signup, name='signup'),
    #  Path for Trip:
    path('trips/', views.trip_list.as_view(), name='trip_list'),
    path('trips/create/', views.trip_create.as_view(), name='trip_create'),
    path('trips/<int:pk>/', views.trip_detail.as_view(), name='trip_detail'),
    path('trips/<int:pk>/delete/', views.trip_delete.as_view(), name='trip_delete'),
    # Path for Recipe:
    path('trips/<int:trip_id>/recipes/', views.recipe_list, name='recipe_list'),
    path('trips/<int:trip_id>/recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('trips/<int:trip_id>/recipes/<int:recipe_id>/save', views.recipe_save, name='recipe_save'),
    # Path for Equipment:
]


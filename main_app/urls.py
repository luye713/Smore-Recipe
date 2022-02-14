from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    #  Path for Trip:
    path('trips/', views.trip_list, name='trip_list'),
    path('trips/create/<int:recipe_id>/', views.trip_create, name='trip_create'),
    path('trips/add/<int:recipe_id>/', views.trip_add, name='trip_add'),
    # path('trips/create/', views.trip_create.as_view(), name='trip_create'),
    path('trips/<int:trip_id>/', views.trip_detail, name='trip_detail'),
    path('trips/<int:pk>/delete/', views.trip_delete.as_view(), name='trip_delete'),
    # Path for Recipe:
    path('recipes/(?P<category>)/(?P<equipment>)', views.recipe_list, name='recipe_list'),
    path('recipes/<slug:category>/<slug:equipment>/', views.recipe_list, name='recipe_list'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('trips/recipes/<int:recipe_id>/', views.recipe_choose, name='recipe_choose'),
    path('trips/<int:trip_id>/recipes/<int:recipe_id>/', views.recipe_save, name='recipe_save'),
    # PDF Download:
    # path('recipes/<int:pk>/pdf/', views.recipe_download.as_view(), name='recipe_download'),
    # Path for Equipment:
]


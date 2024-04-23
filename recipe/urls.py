from django.urls import path

from . import views

app_name='recipe'


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.admin1, name='upload'),
    path('like/<int:recipe_id>/', views.like_recipe, name='like_recipe'),
]


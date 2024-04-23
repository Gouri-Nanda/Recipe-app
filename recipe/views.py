from django.shortcuts import render
from .models import *
from django.conf import settings
from recipe_app.settings import BASE_DIR

def index(request):
    recipes = recipe_data.objects.all()
    return render(request, 'index.html', {'recipe': recipes, 'BASE_DIR': BASE_DIR})

def admin1(request):
    if request.method == 'POST':
        recipe = recipe_data()
        recipe.recipe_name = request.POST.get("recipe_name", "")
        recipe.recipe_desc = request.POST.get("recipe_desc", "")
        recipe.recipe_photo = request.FILES.get("recipe_photo", None)
        if recipe.recipe_photo:
            recipe.save()

    return render(request, 'upload.html')
def like_recipe(request, recipe_id):
    # Perform any necessary validation or checks here
    # For simplicity, we'll just increment the likes count
    recipe = recipe_data.objects.get(pk=recipe_id)
    recipe.likes += 1
    recipe.save()
    return JsonResponse({'likes': recipe.likes})
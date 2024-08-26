from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Recipes
from .forms import RecipesSearchForm
#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin
#to protect function-based views
from django.contrib.auth.decorators import login_required
from .utils import get_recipename_from_id, get_chart


import pandas as pd


# Create your views here.
def home(request):
    return render(request, 'Recipes/home.html')

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipes
    template_name = 'Recipes/recipelist.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipes
    template_name = 'Recipes/recipedetail.html'

def records(request):
    form = RecipesSearchForm(request.POST or None)
    recipe_df = None
    recipe_diff = None
    chart = None
    qs = None
    if request.method == "POST":
        recipe_diff = request.POST.get("recipe_diff")
        chart_type = request.POST.get("chart_type")

        if recipe_diff == "#1":
            recipe_diff = "Easy"
        if recipe_diff == "#2":
            recipe_diff = "Medium"
        if recipe_diff == "#3":
            recipe_diff = "Intermediate"
        if recipe_diff == "#4":
            recipe_diff = "Hard"

        qs = Recipes.objects.all()
        id_searched = []
        for obj in qs:
            diff = obj.calculate_difficulty()
            if diff == recipe_diff:
                id_searched.append(obj.id)

        qs = qs.filter(id__in=id_searched)

        if qs:
            recipe_df = pd.DataFrame(qs.values())
            chart = get_chart(chart_type, recipe_df, labels=recipe_df["name"].values)

            recipe_df = recipe_df.to_html()

    context = {
        "form": form,
        "recipe_df": recipe_df,
        "recipe_diff": recipe_diff,
        "chart": chart,
        "qs": qs,
    }

    return render(request, "Recipes/search.html", context)

from django import forms

DIFFIC_CHOICES = (
    ("#1", "Easy"),
    ("#2", "Medium"),
    ("#3", "Intermediate"),
    ("#4", "Hard"),
)


class RecipesSearchForm(forms.Form):
    recipe_diff = forms.ChoiceField(choices=DIFFIC_CHOICES)
    recipe_name = forms.CharField(max_length=120)

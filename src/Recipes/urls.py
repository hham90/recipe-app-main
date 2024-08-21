from django.urls import path
from .views import home
from .views import RecipeListView
from .views import RecipeDetailView
from .views import records
from django.conf import settings
from django.conf.urls.static import static

app_name = 'recipes'

urlpatterns = [
   path('', home, name='home'),
   path('list/', RecipeListView.as_view(), name='list'),
   path('list/<pk>', RecipeDetailView.as_view(), name='recipedetail'),
   path("search/", records, name="search")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
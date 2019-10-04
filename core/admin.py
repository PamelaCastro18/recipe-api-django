from django.contrib import admin
from .models import User
from .models import Recipe
from .models import Ingredient


admin.site.register(User)
admin.site.register(Ingredient)
admin.site.register(Recipe)


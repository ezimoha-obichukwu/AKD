from django.contrib import admin
from .models import User, Prize, Spin

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "points", "spins_left"]
    list_filter = ["username", "email"]
    search_fields = ["username", "email"]

@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name"]

@admin.register(Spin)
class SpinAdmin(admin.ModelAdmin):
    list_display = ["user", "prize", "timestamp", "is_winner"]
    search_fields = ["user"]

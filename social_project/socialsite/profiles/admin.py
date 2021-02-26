from django.contrib import admin
from .models import Profile, Relationship

# Register your models here.
@admin.register(Profile)
class ProfileAdmind(admin.ModelAdmin):
    list_display = ('id','created')

admin.site.register(Relationship)











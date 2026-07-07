from django.contrib import admin
from .models import Contact, Blog, Skill
# Register your models here.


# Register your models here.
#@admin.site.register(Contact)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('full_name','subject')
    search_fields = ('full_name','subject')
    list_filter = ('created_at',)

admin.site.register(Contact,TaskAdmin)
admin.site.register([Blog,Skill])
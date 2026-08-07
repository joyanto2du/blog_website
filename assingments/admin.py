from django.contrib import admin
from .models import About, SocialLink

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Allow adding only if there are no existing About instances
       # if About.objects.exists():
        #    return False
        #return super().has_add_permission(request)
        count = About.objects.count()
        if count == 0:
            return True  # Allow adding if there are no existing About instances
        return False  # Disallow adding if there is already an About instance


admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)

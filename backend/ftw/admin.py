from django.contrib import admin

from backend.ftw.models import *


class CategoryAdmin(admin.ModelAdmin):

    pass


class LocationAdmin(admin.ModelAdmin):

    pass


class EventAdmin(admin.ModelAdmin):

    pass


class FTWUserAdmin(admin.ModelAdmin):

    pass


class CommentAdmin(admin.ModelAdmin):

    pass


class FTWWordAdmin(admin.ModelAdmin):

    pass

class MediaAdmin(admin.ModelAdmin):

    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(FTWUser, FTWUserAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(FTWWord, FTWWordAdmin)
admin.site.register(Media, MediaAdmin)

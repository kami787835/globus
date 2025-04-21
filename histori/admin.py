from django.contrib import admin
from .models import StoryVideos, Stories, Cards
from django.utils.safestring import  mark_safe


class StoryVideosInline(admin.TabularInline):
    model = StoryVideos
    extra = 1


@admin.register(Stories)
class StoriesAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at")
    list_display_links = list_display
    inlines = (StoryVideosInline,)


@admin.register(Cards)
class CardsAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "type", "datefrom", "dateto", "get_html_img"]
    list_display_links = (
        "id",
        "title",
        "get_html_img",
    )

    def get_html_img(self, object):
        if object.img:
            return mark_safe(f"<img src='{object.img.url}' height='60'>")

    get_html_img.short_description = "Изображение"

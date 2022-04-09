from django.contrib import admin
from .models import Post, Hengst, Sale, PostImage, About, Merrie

admin.site.register(Post)
admin.site.register(Hengst)
admin.site.register(About)
admin.site.register(Merrie)


# Register your models here.
class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Sale)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Sale


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

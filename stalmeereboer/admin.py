from django.contrib import admin
from .models import Post, Hengst, Sale, PostImage, About, Merrie, Veulen, Paard, NieuwsImage, Nieuws

admin.site.register(Post)
admin.site.register(Hengst)
admin.site.register(About)
admin.site.register(Merrie)
admin.site.register(Veulen)
admin.site.register(Paard)


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


class NieuwsImageAdmin(admin.StackedInline):
    model = NieuwsImage


@admin.register(Nieuws)
class NieuwsAdmin(admin.ModelAdmin):
    inlines = [NieuwsImageAdmin]

    class Meta:
        model = Nieuws


@admin.register(NieuwsImage)
class NieuwsImageAdmin(admin.ModelAdmin):
    pass

from django.contrib.auth import get_user_model
from users.models import CustomUser
from django.contrib import admin
from articles.models import Article
# from users.models import CustomUser
#from users.admin import ProfileInline

# CustomUser = get_user_model()

# TODO: Display user details in new table of ArticleAdmin.
# class AuthorInline(admin.TabularInline):
#     model = CustomUser
#     fk_name = "articles"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'tags', 'created_at', 'updated_at']
    list_editable = ['tags']
    # inlines = [
    #     AuthorInline,
    #     ProfileInline,
    # ]


admin.site.register(Article, ArticleAdmin)

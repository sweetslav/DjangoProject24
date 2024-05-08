from django.contrib import admin
from .models import Author, Article, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'category', 'published', 'count_comments')
    list_filter = ('published_date', 'category', 'published')
    search_fields = ['title', 'content']
    readonly_fields = ('published_date',)
    fieldsets = (
        (
            None, {
                'fields': ('title', 'author', 'content', 'category', 'published')
            }
        ),
        (
            'Date Information', {
                'fields': ('published_date',),
                'classes': ('collapse',)
            }
        ),
    )
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(published=True)

    make_published.short_description = "Опубликовать выбранные посты"

    def count_comments(self, obj):
        return obj.count_comments_for_article()

    count_comments.short_description = 'Comments'


class AuthorAdmin(admin.ModelAdmin):
    # Определяем, какие поля будут отображаться в списке объектов
    list_display = ('first_name', 'last_name', 'email', 'birthday')

    # Определяем поля, по которым будет осуществляться поиск
    search_fields = ['first_name', 'last_name', 'email']

    # Группируем поля модели в различные разделы для лучшей организации в административной панели
    fieldsets = (
        # Раздел "Main"
        (
            'Main', {
                'fields': ('first_name', 'last_name', 'email', 'biography')
            }
        ),
        # Раздел "Date Information"
        (
            'Date Information', {
                'fields': ('birthday',),  # Поля в разделе
                'classes': ('collapse',)  # Скрытие раздела по умолчанию
            }
        ),
    )

    # Определяем, какие поля будут доступны только для чтения
    readonly_fields = ('biography',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('get_author_first_name', 'article', 'get_comment_summary', 'created_at', 'updated_at')
    search_fields = ['author__first_name', 'author__last_name', 'article__title']
    readonly_fields = ('created_at', 'updated_at')

    def get_author_first_name(self, obj):
        return obj.author.first_name

    get_author_first_name.short_description = 'Author First Name'

    def get_comment_summary(self, obj):
        words = obj.content.split()[:10]
        return ' '.join(words)

    get_comment_summary.short_description = 'Comment Summary'


admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

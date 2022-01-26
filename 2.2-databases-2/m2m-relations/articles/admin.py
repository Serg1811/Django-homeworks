from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleTag


class ArticleTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        number_of_main = 0
        print(self.cleaned_data)
        for result in self.cleaned_data:
            print(result)
            if result.get('is_main'):
                number_of_main += 1
            if number_of_main > 1:
                raise ValidationError('Основным может быть только один раздел')
        if number_of_main == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    formset = ArticleTagInlineFormset
    extra = 3


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

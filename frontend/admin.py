from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django import forms
from django.utils.safestring import mark_safe
from solo.admin import SingletonModelAdmin
from frontend.models import *


admin.site.unregister(Group)
admin.site.unregister(User)


class ProjectAdminForm(forms.ModelForm):
    description = forms.CharField(label="Description", widget=CKEditorUploadingWidget())


class BlogAdminForm(forms.ModelForm):
    description = forms.CharField(label="Description", widget=CKEditorUploadingWidget())


@admin.register(Configuration)
class ConfigurationAdmin(SingletonModelAdmin):
    pass


@admin.register(Info)
class InfoAdmin(SingletonModelAdmin):
    pass


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = "id", "title", "url"
    list_editable = "title", "url"


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = "title", "short_text", "percent", "icon", "get_icon"
    list_editable = ["percent", "icon"]

    def get_icon(self, obj):
        return mark_safe(f'<img src={obj.icon.url if obj.icon else ""} height="70"')

    get_icon.short_description = "Icon"


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = "id", "name", "email", "avatar", "get_avatar"
    list_editable = "avatar",

    def get_avatar(self, obj):
        return mark_safe(f'<img src={obj.avatar.url if obj.avatar else ""} height="70"')

    get_avatar.short_description = "Avatar"


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = "title", "url", "logo", "get_logo"
    list_editable = "url", "logo"

    def get_logo(self, obj):
        return mark_safe(f'<img src={obj.logo.url} height="70"')

    get_logo.short_description = "Logo"


@admin.register(ResumeCategory)
class ResumeCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = "category", "short_text", "period", "order"
    list_editable = "short_text", "period", "order"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = "title", "category", "short_text", "image", "get_image"
    list_editable = "image", "short_text"

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} height="70"')

    get_image.short_description = "Image"


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    list_display = "title", "category", "short_text", "image", "get_image"
    list_editable = "image", "short_text"

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} height="70"')

    get_image.short_description = "Image"



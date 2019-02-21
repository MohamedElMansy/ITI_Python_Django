from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

UserAdmin.list_display += ('is_active',)
UserAdmin.list_display_links = ('username',)
UserAdmin.list_editable = ('is_active',)
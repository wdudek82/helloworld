from django.contrib import admin

from .models import Example, Hello


class HelloModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'message']

    class Meta:
        model = Hello


class ExampleModelAdmin(admin.ModelAdmin):
    list_display = ['pk', 'tag', 'created_at']

    class Meta:
        model = Example


admin.site.register(Hello, HelloModelAdmin)
admin.site.register(Example, ExampleModelAdmin)

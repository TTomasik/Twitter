from django.contrib import admin
from tweet.models import Tweet, UserExtend
from django.contrib.auth.models import User
# Register your models here.

@admin.register(UserExtend)
class ClassUserExtend(admin.ModelAdmin):
    list_display = ('user', 'image_url')

    def image_url(self, obj):
        return "<img src ='/{}' width='150' height='150' >".format(obj.avatar)

    image_url.allow_tags = True

@admin.register(Tweet)
class AdminTweet(admin.ModelAdmin):
    list_display = ('content', 'creation_date', 'user')
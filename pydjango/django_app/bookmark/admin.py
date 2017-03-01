from django.contrib import admin

from bookmark.models import Bookmark


# Admin 사이트에서 Bookmark 내용을 보여주는 클래스
class BookmarkAdmin(admin.ModelAdmin):
    # title, url 을 화면에 출력
    list_display = ('title', 'url')


# admin.site.register() 함수를 사용해 Bookmark, BookmarkAdmin 클래스를 등록
admin.site.register(Bookmark, BookmarkAdmin)

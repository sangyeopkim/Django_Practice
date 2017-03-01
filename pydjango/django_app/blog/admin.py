from django.contrib import admin

from blog.models import Post


# PostAdmin 클래스는 Post 클래스가 Admin 사이트에서 어떤 모습으로 보여줄지를 정의하는 클래스
class PostAdmin(admin.ModelAdmin):
    # Post 객체를 보여줄 때 title, modify_date 를 화면에 출력
    list_display = ('title', 'modify_date')
    # modify_date 컬럼을 사용하는 필터 사이드바를 보여주도록 지정
    list_filter = ('modify_date',)
    # 검색박스를 표시하고, 입력된 단어는 title, content 컬럼에서 검색하도록 지정
    search_fields = ('title', 'content')
    # slug 필드는 title 필드를 사용해 미리 채워지도록 함
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)

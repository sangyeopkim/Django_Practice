from django.conf.urls import url

from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
    # /bookmark/ 요청을 처리할 뷰 클래스 지정
    # URL 패턴의 이름은 namespace 를 포함해 'bookmark:index' 가 된다
    url(r'^$', BookmarkLV.as_view(), name='index'),
    # URL /bookmark/숫자/ 요청을 처리할 뷰 클래스 지정
    # 숫자 자리에는 레코드의 기본 키가 들어간다
    # URL 패턴의 이름은 namespace 를 포함해 'bookmark:detail' 이 된다
    url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view, name='detail')
]

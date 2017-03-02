from django.conf.urls import url
from blog.views import *
urlpatterns = [
    # Example: /
    # URL /blog/ 요청을 처리할 뷰 클래스를 PostLV 로 지정
    # URL 패턴 이름은 namespace 를 포함해 'blog:index' 가 된다
    url(r'^$', PostLV.as_view(), name='index'),

    # Example: /post/ (same as /)
    # URL /blog/post/ 요청을 처리할 뷰 클래스를 PostLV 로 지정
    # URL 패턴 이름은 namespace 를 포함해 'blog:index' 가 된다
    # PostLV 뷰 클래스는 '/blog/' 와 '/blog/post/' 2 가지의 요청을 모두 처리한다
    url(r'^post/$', PostLV.as_view(), name='post_list'),

    # Example: /post/django-example/
    # URL /blog/post/영단어/ 요청을 처리할 뷰 클래스를 PostDV 로 지정
    # URL 패턴 이름은 namespace 를 포함해 'blog:detail' 이 된다
    url(r'^post/(?P<slug>[-w]+)/$', PostDV.as_view(), name='post_detail'),

    # Example: /archive/
    # URL /blog/archive/ 요청을 처리할 뷰 클래스를 PostAV 로 지정
    # URL 패턴 이름은 namespace 를 포함해 'blog:archive' 가 된다
    url(r'^archive/$', PostAV.as_view(), name='post_archive'),

    # Example: /2012/
    # URL /blog/4자리 숫자/ 요청을 처리할 뷰 클래스를 PostYAV 로 지정
    # URL 패턴 이름은 namespace 를 포함해 'blog:post_year_archive' 가 된다
    url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),

    # Example: /2012/nov/
    # URL /blog/4자리 숫자/3자리 소문자/ 요청을 처리할 뷰 클래스를 PostMAV 로 지정
    # URL 패턴 이름은 namespace 를 포함해 'blog:post_month_archive' 가 된다
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),

    # Example: /2012/nov/10/
    # URL /blog/4자리 숫자/3자리 소문자/1~2자리 숫자/ 요청을 처리할 뷰 클래스를 PostDAV 로 지정
    # URL 패턴 이름은 namespace 를 포함해 'blog:post_day_archive' 가 된다
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),

    # Example: /today/
    # URL /blog/today/ 요청을 처리할 뷰 클래스를 PostTAV 로 지정
    # URL 패턴 이름은 namespace 를 포함해 'blog:post_today_archive' 가 된다
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),
]
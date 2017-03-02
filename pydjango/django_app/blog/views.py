from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, \
    TodayArchiveView

from blog.models import Post


# ListView
# ListView 제네릭 뷰를 상속받아 PostLV 클래스형 뷰를 정의
# 테이블로부터 객체 리스트를 가져와 그 리스트를 출력
class PostLV(ListView):
    # PostLV 클래스의 대상 테이블은 Post 테이블이다
    model = Post
    # 테플릿 파일은 'blog/post_all.html' 로 지정
    template_name = 'blog/post_all.html'
    # 테플릿 파일로 넘겨주는 객체 리스트에 대한 컨텍스트 변수명을 'posts' 로 지정
    context_object_name = 'posts'
    # 한 페이지에 보여주는 객체 리스트의 숫자는 2
    paginate_by = 2


# DetailView
# DetailView 제네릭 뷰를 상속받아 PostDV 클래스형 뷰를 정의
# 테이블로부터 특정 객체를 가져와 그 객체의 상세 정보를 출력
# 테이블에서 특정 객체를 조회하기 위한 키는 기본 키 대신 slug 속성을 사용하고 있다
# 이 slug 파라미터는 URLconf 에서 추출해 뷰로 넘겨준다
class PostDV(DetailView):
    # PostDV 클래스의 대상 테이블은 Post 테이블이다
    mode = Post


# ArchiveView
# ArchiveIndexView 제네릭 뷰를 상속받아 PostAV 클래스형 뷰를 정의
# 테이블로부터 객체 리스트를 가져와, 날짜 필드를 기준으로 최신 객체를 먼저 출력
class PostAV(ArchiveIndexView):
    model = Post
    # 기준이 되는 날짜 필드는 'modify_date' 컬럼을 사용
    # 즉, 변경 날짜가 최근인 포스트를 먼저 출력
    date_filed = 'modify_date'


# YearArchiveView 제네릭 뷰를 상속받아 PostYAV 클래스형 뷰를 정의
# 테이블로부터 날짜 필드의 연도를 기준으로 객체 리스트를 가져와, 그 객체들이 속한 월을 리스트로 출력
# 날짜 필드의 연도 파라미터는 URLconf 에서 추출해 뷰로 넘겨준다
class PostYAV(YearArchiveView):
    model = Post
    # 기준이 되는 날짜 필드는 'modify_date' 컬럼을 사용
    # 즉, 변경 날짜가 YYYY 연도인 포스트를 검색해, 그 포스트들의 변경 월을 출력
    date_field = 'modify_date'
    # True 이면 해당 년도에 해당하는 객체의 리스트를 만들어서 템플릿에 넘겨준다
    # 즉, 템플릿 파일에서 object_list 컨텍스트 변수를 사용할 수 있다
    # 디폴트는 False
    make_object_list = True


# MonthArchiveView 제네릭 뷰를 상속받아 PostMAV 클래스형 뷰를 정의
# 테이블로 부터 날짜 필드의 연월을 기준으로 객체 리스트를 가져와, 그 리스트를 출력
# 날짜 필드의 연도 및 월 파라미터는 URLconf 에서 추출해 뷰로 넘겨준다
class PostMAV(MonthArchiveView):
    model = Post
    # 기준이 되는 날짜 필드는 'modify_date' 컬럼을 사용
    # 즉, 변경 날짜의 연월을 기준으로 포스트를 검색해 그 포스트들의 리스트를 출력
    date_field = 'modify_date'


# DayArchiveView 제네릭 뷰를 상속받아 PostDAV 클래스형 뷰를 정의
# 테이블로부터 날짜 필드의 연월일을 기준으로 객체 리스트를 가져와 그 리스트를 출력
# 날짜 필드의 연도, 월, 일 파라미터는 URLconf 에서 추출해 뷰로 넘거준다
class PostDAV(DayArchiveView):
    model = Post
    # 변경 날짜의 연월일을 기준으로 포스트를 검색해 그 포스트들의 리스트를 출력
    date_filed = 'modify_date'


# TodayArchiveView 제네릭 뷰를 상속받아 PostTAV 클래스형 뷰를 정의
# 테이블로부터 날짜 필드가 오늘인 객체 리스트를 가져와, 그 리스트를 출력
# 오늘 날짜를 기준 연월일로 지정한다는 점 외에는 DayArchiveView 와 동일
class PostTAV(TodayArchiveView):
    model = Post
    # 변경 날짜가 오늘인 포스트를 검색해, 그 포스트들의 리스트를 출력
    date_field = 'modify_date'

# 제네릭 뷰의 강력함을 볼 수 있음
# 페이징 기능이나, 날짜 기반 제네릭 뷰를 직접 코딩하지 않아도 된다 (모두 장고에서 처리)

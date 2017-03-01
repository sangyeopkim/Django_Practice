from django.db import models
from django.urls import reverse


class Post(models.Model):
    # title 컬럼에 대한 레이블은 TITLE 이고, 최대 길이는 50글자
    # 레이블은 폼 화면에 나타나는 문구로, Admin 사이트에서 확인 가능
    title = models.CharField('TITLE', max_length=50)

    # slug 컬럼은 제목의 별칭
    # SlugField 에 unique 옵션을 추가해 특정 포스트를 검색 시 기본 키 대신에 사용
    # allow_unicode 옵션을 추가하면 한글 처리가 가능
    # help_text 는 해당 컬럼을 설명해주는 문구로 폼 화면에 나타남. Admin 사이트에서 확인 가능
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')

    # description 컬럼은 빈칸 허용
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')

    # content 컬럼은 TextField 를 사용하였고, 여러 줄 입력이 가능
    content = models.TextField('CONTENT')

    # 날짜와 시간을 입력하는 DateTimeField
    # auto_now_add 속성은 객체가 생성될 때의 시각을 자동으로 기록
    create_date = models.DateTimeField('Create Date', auto_now_add=True)

    # 날짜와 시간을 입력하는 DateTimeField
    # auto_now 속성은 객체가 데이터베이스에 저장될 때의 시각을 자동으로 기록. 즉, 객체가 변경될 때 마다 시각이 기록 됨
    modify_date = models.DateTimeField('Modify Date', auto_now=True)

    # 필드 속성 외에 필요한 파라미터가 있으면, Meta 내부 클래스로 정의
    class Meta:
        # 테이블의 별칭을 단수와 복수로 가질 수 있는데, 단수 별칭을 'post' 로 한다
        verbose_name = 'post'
        # 테이블의 복수 별칭을 'posts' 로 한다
        verbose_name_plural = 'posts'
        # 데이터베이스에 저장되는 테이블의 이름을 'my_post' 로 지정
        # 이 항목을 생략하면 디폴트는 '앱명_모델클래스명'을 테이블명으로 지정한다
        # 즉, db_table 항목을 지정하지 않았다면, blog_post 가 되었을 것이다
        db_table = 'my_post'
        # 모델 객체의 리스트 출력 시, modify_date 컬럼을 기준으로 내림차순으로 정렬
        ordering = ('-modify_date',)

    # 객체의 문자열을 객체.title 속성으로 표시되도록 함
    def __str__(self):
        return self.title

    # 이 메소드가 정의된 객체를 지칭하는 URL 을 반환
    # 메소드 내에서는 django 의 내장함수인 reverse() 를 호출
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    # modify_date 컬럼을 기준으로 이전 포스트를 반환
    # 메소드 내에서는 django 의 내장함수인 get_previous_by_modify_date() 를 호출
    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    # modify_date 컬럼을 기준으로 다음 포스트를 반환
    # 메소드 내에서는 django 의 내장함수인 get_next_by_modify_date() 를 호출
    def get_next_post(self):
        return self.get_next_by_modify_date()

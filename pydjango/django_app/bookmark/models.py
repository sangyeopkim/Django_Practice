from django.db import models


class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)

    # 객체를 문자열로 표현할 때 사용하는 함수
    # 이 함수를 정의하지 않으면, Admin 사이트나 장고 셸 등에서 테이블명이 제대로 표현되지 않는다.
    def __str__(self):
        return self.title
        # return "%s %s" %(self.title, self.url)

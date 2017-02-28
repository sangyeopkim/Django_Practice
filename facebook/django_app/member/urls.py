from . import views
from django.conf.urls import url

app_name = 'member'
urlpatterns = [
    url(r'^login/', views.login_fbv, name='login')
]

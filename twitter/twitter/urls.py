"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from tweet.views import index, LoginView, TweetView, AddTweet, MyInfo, ContentAll
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^logout/$', logout_then_login, name='site-logout'),
    url(r'^login/?$', LoginView.as_view(), name='login'),
    url(r'^welcome/?$', TweetView.as_view(), name='welcome'),
    url(r'^add_tweet/?$', AddTweet.as_view(), name='add-tweet'),
    url(r'^my_info/(?P<person_id>(\d){1,4})$', MyInfo.as_view(), name='my-info'),
    url(r'^content_all/?$', ContentAll.as_view(), name='content-all'),
]

from django.conf.urls import patterns, include, url
from mysite.views import hello, my_home_view, current_datetime, hours_ahead, more_practice, factorial
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', my_home_view),
    url(r'^hello/$', hello),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^date/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^factorial/(\d{1})/$', more_practice)
)



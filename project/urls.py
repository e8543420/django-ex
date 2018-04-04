from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from chatterbot.ext.django_chatterbot import urls as chatterbot_urls
from example_app.views import ChatterBotAppView

from welcome.views import index, health

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', ChatterBotAppView.as_view(), name='main'),
	url(r'^help/',index),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^api/chatterbot/', include(chatterbot_urls, namespace='chatterbot')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

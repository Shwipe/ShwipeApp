from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from shwipe.views import *

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    (r'^accounts/', include('allauth.urls')),
    #url(r'^$', 'shwipe.views.home', name='home'),
    #url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', ProductListView.as_view(), name='product-list'),
) 


# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += patterns('django.contrib.staticfiles.views',
#         #url(r'^(?:index.html)?$', 'serve', kwargs={'path': 'index.html'}),
#         url(r'^(?P<path>(?:js|css|img)/.*)$', 'serve'),
#     )

# https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#adminsite-attributes
admin.site.site_header = 'Shwipe Admin'
admin.site.site_title = 'Shwipe Admin'
admin.site.site_url = None # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.AdminSite.site_url


""" Notes
 - https://docs.djangoproject.com/en/1.8/intro/tutorial03/#write-your-first-view
 - http://django-suit.readthedocs.org/en/develop/#
"""
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

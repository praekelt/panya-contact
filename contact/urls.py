from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'contact.views',
    url(r'^$', 'site_contact', name='site_contact'),
)

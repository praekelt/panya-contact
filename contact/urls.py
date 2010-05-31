from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'contact.views',
    url(r'^$', 'generic_contact_page', name='contact'),
)

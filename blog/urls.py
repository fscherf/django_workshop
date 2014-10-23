from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^add/$', 'add_post', name='add_post'),
    url(r'^(?P<post_id>\d+)/$', 'view_posts', name='view_posts'),
    url(r'^$', 'view_posts', name='view_posts'),
)

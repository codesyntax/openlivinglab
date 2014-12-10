from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    #To completely get openlivinlab.com in your environment
    url(r'', include('smartlivinglab.urls')),
)

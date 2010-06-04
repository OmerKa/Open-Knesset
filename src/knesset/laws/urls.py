#encoding: UTF-8
from django.conf.urls.defaults import *
from django.utils.translation import ugettext
from knesset.hashnav.views import ListDetailView
from models import *
from views import *

vote_view = VoteListView(queryset = Vote.objects.all(),paginate_by=20, extra_context={'votes':True,'title':ugettext('Votes')})
law_view = LawView(queryset=Law.objects.filter(title__contains='חוק').order_by('title'), paginate_by=20, extra_context={'title':ugettext('Laws')})

lawsurlpatterns = patterns ('',
    url(r'^law/$', law_view, name='law-list'),
    url(r'^law/(?P<object_id>\d+)/$', law_view, name='law-detail'),
    url(r'^vote/$', vote_view, name='vote-list'),
    url(r'^vote/(?P<object_id>\d+)/submit-tags/$', submit_tags),
    url(r'^vote/(?P<object_id>\d+)/suggest-tag/$', suggest_tag),
    url(r'^vote/(?P<object_id>\d+)/tag-votes/(?P<tag_id>\d+)/(?P<vote>[+\-\d]+)/$', vote_on_tag),  
    url(r'^vote/(?P<object_id>\d+)/$', vote_view, name='vote-detail'),
    url(r'^votes/tagged/(?P<tag>.*)/$', tagged, name='tagged-votes'),    
)

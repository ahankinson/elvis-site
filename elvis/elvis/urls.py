from django.conf.urls import patterns, include, url, static
from django.conf import settings

from rest_framework.urlpatterns import format_suffix_patterns

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from elvis.views.main import home
from elvis.views.main import upload
from elvis.views.main import save_downloads
from elvis.views.main import user_profiles, user_view
from elvis.views.main import projects_list, project_view, project_participants, project_discussions, discussion_view
from elvis.views.main import search_view, queries
from elvis.views.main import corpora_list, corpus_view
from elvis.views.main import composer_list, composer_view
from elvis.views.main import piece_list, piece_view
from elvis.views.main import movement_list, movement_view

from elvis.views.search import search
from elvis.views.search import search_results

from elvis.views.download import DownloadList, DownloadDetail
from elvis.views.piece import PieceList, PieceDetail
from elvis.views.corpus import CorpusList, CorpusDetail
from elvis.views.user import UserList, UserDetail
from elvis.views.userprofile import UserProfileList, UserProfileDetail
from elvis.views.movement import MovementList, MovementDetail
from elvis.views.composer import ComposerList, ComposerDetail
from elvis.views.tag import TagList, TagDetail
from elvis.views.attachment import AttachmentList, AttachmentDetail

from elvis.views.forms import create_composer, create_corpus
from elvis.views.forms import upload_file


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = []

urlpatterns += format_suffix_patterns(
    patterns('',
        url(r'^$', home, name='home'),
        url(r'^users/$', UserList.as_view(), name="user-list"),
        url(r'^user/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name="user-detail"),

        #url(r'^userprofiles/$', UserProfileList.as_view(), name="userprofile-list"),
        url(r'^userprofiles/$', user_profiles, name="userprofile-list"),
        #url(r'^userprofiles/(?P<pk>[0-9]+)/$', UserProfileDetail.as_view(), name="userprofile-detail"),
        url(r'^userprofiles/(?P<pk>[0-9]+)/$', user_view, name="userprofile-detail"),

        url(r'^projects/$', projects_list, name="projects-list"),
        url(r'^projects/(?P<pk>[0-9]+)/$', project_view, name="project-detail"),
        url(r'^projects/(?P<pk>[0-9]+)/participants$', project_participants, name="project-participants"),
        url(r'^projects/(?P<pk>[0-9]+)/discussions$', project_discussions, name="project-discussions"),
        url(r'^projects/(?P<pk>[0-9]+)/discussions/(?P<did>[0-9]+)$', discussion_view, name="project-discussions"),

        #url(r'^pieces/$', PieceList.as_view(), name="piece-list"),
        #url(r'^piece/(?P<pk>[0-9]+)/$', PieceDetail.as_view(), name="piece-detail"),
        #url(r'^corpora/$', CorpusList.as_view(), name="corpus-list"),
        #url(r'^corpus/(?P<pk>[0-9]+)/$', CorpusDetail.as_view(), name="corpus-detail"),
        #url(r'^composers/$', ComposerList.as_view(), name="composer-list"),
        #url(r'^composer/(?P<pk>[0-9]+)/$', ComposerDetail.as_view(), name="composer-detail"),
        #url(r'^movements/$', MovementList.as_view(), name="movement-list"),
        #url(r'^movement/(?P<pk>[0-9]+)/$', MovementDetail.as_view(), name="movement-detail"),

        url(r'^pieces/$', piece_list, name="piece-list"),
        url(r'^pieces/(?P<pk>[0-9]+)/$', piece_view, name="piece-detail"),
        url(r'^corpora/$', corpora_list, name="corpus-list"),
        url(r'^corpora/(?P<pk>[0-9]+)/$', corpus_view, name="corpus-detail"),
        url(r'^composers/$', composer_list, name="composer-list"),
        url(r'^composers/(?P<pk>[0-9]+)/$', composer_view, name="composer-detail"),
        url(r'^movements/$', movement_list, name="movement-list"),
        url(r'^movements/(?P<pk>[0-9]+)/$', movement_view, name="movement-detail"),
        
        url(r'^tags/$', TagList.as_view(), name="tag-list"),
        url(r'^tag/(?P<pk>[0-9]+)/$', TagDetail.as_view(), name="tag-detail"),

        url(r'^search/$', search, name="search"),
        url(r'^search_results/$', search_view, name="search_results"),
        url(r'^upload/$', upload_file, name="upload"),

        url(r'^queries/$', queries, name="queries"),

        url(r'^addcomposer/$', create_composer, name="create-composer"),
        url(r'^addcorpus/$', create_corpus, name="create-corpus"),

        url(r'^downloads/$', DownloadList.as_view(), name="download-list"),
        url(r'^download/(?P<pk>[0-9]+)/$', DownloadDetail.as_view(), name="download-detail"),
        #url(r'^download/$', save_downloads, name="save_downloads"),
        #url(r'^download/$', DownloadList.as_view(), name="download-list"),
        
        url(r'^attachments/$', AttachmentList.as_view(), name="attachment-list"),
        url(r'^attachment/(?P<pk>[0-9]+)/$', AttachmentDetail.as_view(), name="attachment-detail"),
    )
)

# Serving static files
#urlpatterns += staticfiles_urlpatterns()

# Media stuff
urlpatterns += patterns('', 
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

# Only add admin if it's enabled
if 'django.contrib.admin' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^admin/', include(admin.site.urls)),
    )


# For serving stuff under MEDIA_ROOT in debug mode only
# if settings.DEBUG:
#     urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import url
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework_jwt.views import obtain_jwt_token

from django.contrib import admin

from backend.ftw.views import FileUploadView
from . import views

schema_view = get_schema_view(
    openapi.Info(
        title='API',
        default_version='v1'
    ),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # EVENT
    path('event/list', views.event_list),
    path('event/create', views.event_form_create),
    path('event/<int:pk>/get', views.event_form_get),
    path('event/<int:pk>/update', views.event_form_update),
    path('event/<int:pk>/delete', views.event_delete),

    # LOCATION
    #path('location/list', views.location_list),
    path('location/create', views.location_form_create),
    path('location/<int:pk>/get', views.location_form_get),
    path('location/<int:pk>/update', views.location_form_update),
    path('location/<int:pk>/delete', views.location_delete),

    #CATEGORY
    #path('category/list', views.category_list),
    path('category/create', views.category_form_create),
    path('category/<int:pk>/get', views.category_form_get),
    path('category/<int:pk>/update', views.category_form_update),
    path('category/<int:pk>/delete', views.category_delete),

    # COMMENT
    path('comment/create', views.comment_form_create),
    path('comment/<int:pk>/update', views.comment_form_update),
    path('comment/<int:pk>/delete', views.comment_delete),

    # FTWWord
    path('ftwword/list', views.ftwword_list),

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    url(r'^api-token-auth/', obtain_jwt_token),

    url(r'^media$', FileUploadView.as_view()),
    path('media/<int:pk>', views.media_download),
    path('media/<int:pk>/get', views.media_get),
]

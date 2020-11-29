# {% comment %}
#
# from django.contrib import admin
# from django.urls import path, re_path, include
#
# from . import views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     re_path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider'))
# ]
#
# {% endcomment %}

from django.contrib import admin

from django.conf.urls import url, include
import oauth2_provider.views as oauth2_views
from django.conf import settings
from .views import ApiEndpoint

from django.urls import path, re_path, include

# OAuth2 provider endpoints
oauth2_endpoint_views = [
    path('authorize/', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    path('token/', oauth2_views.TokenView.as_view(), name="token"),
    path('revoke-token/', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
]

if settings.DEBUG:
    # OAuth2 Application Management endpoints
    oauth2_endpoint_views += [
        path('applications/', oauth2_views.ApplicationList.as_view(), name="list"),
        path('applications/register/', oauth2_views.ApplicationRegistration.as_view(), name="register"),
        path('applications/<pk>/', oauth2_views.ApplicationDetail.as_view(), name="detail"),
        path('applications/<pk>/delete/', oauth2_views.ApplicationDelete.as_view(), name="delete"),
        path('applications/<pk>/update/', oauth2_views.ApplicationUpdate.as_view(), name="update"),
    ]

    # OAuth2 Token Management endpoints
    oauth2_endpoint_views += [
        path('authorized-tokens/', oauth2_views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
        path('authorized-tokens/<pk>/delete/', oauth2_views.AuthorizedTokenDeleteView.as_view(), name="authorized-token-delete"),
    ]

urlpatterns = [

    path('admin/', admin.site.urls),

    # OAuth 2 endpoints:
    # path('o/', include(oauth2_endpoint_views, namespace="oauth2_provider"), name="oauth2_endpoint_views"),

    path('api/hello', ApiEndpoint.as_view()),  # an example resource endpoint
]

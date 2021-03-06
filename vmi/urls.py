"""vmi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import (
    path,
    include,
)
from django.conf.urls import url
from oauth2_provider import views as oauth2_views
from apps.oidc import views as oidc_views
from apps.home.views import authenticated_home

oauth2_base_urlpatterns = [
    url(r"^authorize/$",
        oidc_views.AuthorizationView.as_view(),
        name="authorize"),
    url(r"^token/$",
        oauth2_views.TokenView.as_view(),
        name="token"),
    url(r"^revoke_token/$",
        oauth2_views.RevokeTokenView.as_view(),
        name="revoke-token"),
    url(r"^introspect/$",
        oauth2_views.IntrospectTokenView.as_view(),
        name="introspect"),
]


oauth2_management_urlpatterns = [
    # Application management views
    url(r"^applications/$",
        oauth2_views.ApplicationList.as_view(),
        name="list"),
    url(r"^applications/register/$",
        oauth2_views.ApplicationRegistration.as_view(),
        name="register"),
    url(r"^applications/(?P<pk>[\w-]+)/$",
        oauth2_views.ApplicationDetail.as_view(),
        name="detail"),
    url(r"^applications/(?P<pk>[\w-]+)/delete/$",
        oauth2_views.ApplicationDelete.as_view(),
        name="delete"),
    url(r"^applications/(?P<pk>[\w-]+)/update/$",
        oauth2_views.ApplicationUpdate.as_view(),
        name="update"),
    # Token management views
    url(r"^authorized_tokens/$",
        oauth2_views.AuthorizedTokensListView.as_view(),
        name="authorized-token-list"),
    url(r"^authorized_tokens/(?P<pk>[\w-]+)/delete/$",
        oauth2_views.AuthorizedTokenDeleteView.as_view(),
        name="authorized-token-delete"),
]


urlpatterns = [
    path('admin/',
         admin.site.urls),
    path('o/',
         include((oauth2_management_urlpatterns + oauth2_base_urlpatterns,
                 'oauth2_provider'))),
    path('auth/',
         include('django.contrib.auth.urls')),
    path('accounts/',
         include('apps.accounts.urls')),
    path('.well-known/',
         include('apps.oidc.wellknown_urls')),
    path('o/', include(('apps.oidc.urls', 'oidc'), namespace='oidc')),
    path('', authenticated_home, name='home'),
]

"""master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin


#admin url
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

#website url
urlpatterns += [
    url(r'^maryknoll/', include('maryknoll.urls')),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
        url(r'^accounts/', include('django.contrib.auth.urls')),
    ]
    
    
'''This automatically adds:
    ^accounts/login/$ [name='login']
    ^accounts/logout/$ [name='logout']
    ^accounts/password_change/$ [name='password_change']
    ^accounts/password_change/done/$ [name='password_change_done']
    ^accounts/password_reset/$ [name='password_reset']
    ^accounts/password_reset/done/$ [name='password_reset_done']
    ^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
    ^accounts/reset/done/$ [name='password_reset_complete']
'''
"""pro_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from issue import views as issue_views
#for static files, change during production
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from ckeditor_uploader import views
from django.conf.urls import url
from django.views.decorators.cache import never_cache
import notifications.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('issue/', include('issue.urls')),
    path('register/',user_views.register, name="register"),
    path('user/<str:username>/',issue_views.UserIssue, name="user-issues"),
    path('user/<str:username>/archives/',issue_views.UserIssueArchives, name="old-user-issues"),
    path('update_profile/',user_views.update_profile, name="update_profile"),
    path('profile/',user_views.profile, name="profile"),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('markdownx/', include('markdownx.urls')),
    #path('ckeditor/', include('ckeditor_uploader.urls'))
    url(r'^ckeditor/upload/', login_required(views.upload), name='ckeditor_upload'),
    url(r'^ckeditor/browse/', never_cache(login_required(views.browse)), name='ckeditor_browse'),
    path('',user_views.dashboard, name="dashboard"),
    path('priority_data/', user_views.result_data, name="priority"),
    path('finished_data/', user_views.finished_data, name="finished"),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('notifications/', include('notice.urls', namespace='notice'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
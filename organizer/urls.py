"""organizer URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from tasks.views import TaskUpdateView, TaskDeleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'tasks.views.tasks_list', name='week_plan'),
    url(r'^start/', 'tasks.views.start', name='start'),
    url('^social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'start'}, name='auth_logout'),
    # register users namespace
    url(r'^users/', include('registration.backends.simple.urls', namespace='users')),
    url(r'^add_task/', 'tasks.views.task_add', name='add_task'),
    url(r'^(?P<pk>\d+)/edit/$', TaskUpdateView.as_view(), name='edit_task'),
    url(r'^(?P<pk>\d+)/delete/$', TaskDeleteView.as_view(), name='delete_task'),
]

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("", views.HomeView.as_view(), name='home'),
    path("project/<slug:slug>", views.ReceiveProjectView.as_view(), name='project'),
    path("blog/<slug:slug>", views.ReceiveBlogView.as_view(), name='blog'),
    path("message/", views.ReceiveMessage.as_view(), name='message'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

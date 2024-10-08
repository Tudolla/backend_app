
from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('user_auth.urls')),
    path('api/v1/', include('contribution.urls')),
    path('api/v1/', include('time_tracking.urls')),
    path('api/v1/', include('stories.urls')),
    path('api/v1/', include('company.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
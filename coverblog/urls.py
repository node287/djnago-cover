from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

import DetailPage.urls
import ProjectPage.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(DetailPage.urls)),
    path('projects/', include(ProjectPage.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from pages.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    

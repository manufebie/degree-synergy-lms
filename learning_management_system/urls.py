from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from pages.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('events/', include('scheduler.urls')),
]

if settings.DEBUG:
    '''Only import debug_toolbar in if Debug is TRUE'''
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    

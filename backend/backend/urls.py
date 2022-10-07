from django.conf.urls import handler400, handler403, handler404, handler500
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('app.urls')),
    path('admin/', include('adminApp.urls')),
    path('user/', include('userApp.urls')),
    # path('auth/', include('authentication.urls')),
    # path('static/', include('static')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# handler404 = 'backend.views.error_404'
# handler500 = 'backend.views.error_500'
# handler403 = 'backend.views.error_403'
# handler400 = 'backend.views.error_400'


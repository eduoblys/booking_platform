from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
import debug_toolbar

urlpatterns = [

    path('admin/', admin.site.urls),
]
urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),

    path('', include('booking.urls')),
    path('manager/', include('manager.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    prefix_default_language=False,
)

if settings.DEBUG:

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]


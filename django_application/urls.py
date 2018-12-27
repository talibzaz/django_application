from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from drogo import views as drogo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drogo/', include('drogo.urls')),
    path('accounts/', include('accounts.urls')),
    path('email_account/', include('email_account.urls', namespace='email_account')),
    path('', drogo_views.article_list, name='home')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

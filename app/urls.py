# django_project/urls.py
from django.contrib import admin
from django.urls import path, include, re_path  # new
from django.views.generic.base import TemplateView  # new
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),  # signup
    path("accounts/", include("django.contrib.auth.urls")),  # login,logout
    path("", TemplateView.as_view(template_name="home.html"), name="home"),  # new
    path("categories/", include('catalog.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         re_path(r'^__debug__/', include(debug_toolbar.urls)),  # updated
#     ] + urlpatterns
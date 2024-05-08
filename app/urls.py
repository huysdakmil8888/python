# django_project/urls.py
from django.urls import path, include, re_path  # new
from django.views.generic.base import TemplateView  # new
from django.conf import settings
from django.conf.urls.static import static
from catalog.admin import admin_site
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from app.views import HomeView

schema_view = get_schema_view(
   openapi.Info(
      title="Your API",
      default_version='v1',
      description="API documentation",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin_site.urls),
    path("accounts/", include("accounts.urls")),  # signup
    path("accounts/", include("django.contrib.auth.urls")),  # login,logout
    path("", HomeView.as_view(template_name="home.html"), name="home"),  # new
    path("catalog/", include('catalog.urls')),
    path('api/', include('api.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
    # Endpoint để lấy token
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Endpoint để làm mới token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         re_path(r'^__debug__/', include(debug_toolbar.urls)),  # updated
#     ] + urlpatterns
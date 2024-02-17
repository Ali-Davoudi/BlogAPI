from django.contrib import admin
from django.urls import path, include

from drf_spectacular import views as api_doc_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('posts.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/schema/', api_doc_view.SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/redoc/', api_doc_view.SpectacularRedocView.as_view(), name='redoc'),
    path('api/schema/swagger-ui/', api_doc_view.SpectacularSwaggerView.as_view(), name='swagger_ui'),
]

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import stripe_webhook, upi_webhook

schema_view = get_schema_view(
   openapi.Info(
      title="GetIt API",
      default_version='v1',
      description="API Documentation"
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', include('auth.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/events/', include('events.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/products/', include('products.urls')),
    path('api/tickets/', include('tickets.urls')),
    path('api/stripe/webhook/', stripe_webhook, name='stripe-webhook'),
    path('api/upi/webhook/', upi_webhook, name = 'upi-webhook'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

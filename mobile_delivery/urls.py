# from django.urls import include, path
# from rest_framework import routers
# from . import views

# router = routers.DefaultRouter()
# # router.register(r'delivery', views.DeliverySerializer,basename='delivery')

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('/api', include(router.urls)),
#      path('api/instances/', views.DeliverySerializer.as_view(), name="instances"),
# ]
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('api/delivery', views.DeliveryViewSet,basename="delivery")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
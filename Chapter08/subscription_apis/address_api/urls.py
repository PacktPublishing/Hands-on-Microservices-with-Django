
# ModelViewSet-based view
from django.urls import include, path
from rest_framework import routers
from .views import AddressViewSet

ver = 'v1'

router = routers.DefaultRouter()
router.register(f'api/{ver}/addresses', AddressViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# APIView + Mixins + Generic class-based views
# from django.urls import include, path
# from .views import AddressList, AddressDetail
#
# ver = 'v1'
#
# urlpatterns = [
#     path(f'api/{ver}/addresses/', AddressList.as_view()),
#     path(f'api/{ver}/addresses/<int:pk>/', AddressDetail.as_view()),
# ]

# Function-based views
# from django.urls import path
# from .views import address_list_view, address_detail_view
#
# ver = 'v1'
#
# urlpatterns = [
#     path(f'api/{ver}/addresses/', address_list_view),
#     path(f'api/{ver}/addresses/<int:pk>/', address_detail_view),
# ]

# ModelViewSet-based view
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Address
from .serializers import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by("name")
    serializer_class = AddressSerializer
    permission_classes = [AllowAny]

# APIView-based view
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Address
# from .serializers import AddressSerializer
# class AddressList(APIView):
#     def get(self, request, format=None):
#         addresses = Address.objects.all()
#         serializer = AddressSerializer(addresses, many=True)
#         return Response(serializer.data)
#     def post(self, request, format=None):
#         serializer = AddressSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Mixins
# from rest_framework import mixins
# from rest_framework import generics
# from .models import Address
# from .serializers import AddressSerializer
#
# class AddressList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
# class AddressDetail(mixins.RetrieveModelMixin,
#                     mixins.CreateModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#     def patch(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# Generic class-based views
# from rest_framework import generics
# from .models import Address
# from .serializers import AddressSerializer
#
# class AddressList(generics.ListCreateAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer
#
# class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer


# Function-based views
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Address
# from .serializers import AddressSerializer
#
# @api_view(['GET', 'POST'])
# def address_list_view(request):
#     if request.method == 'GET':
#         addresses = Address.objects.all()
#         serializer = AddressSerializer(addresses, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = AddressSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def address_detail_view(request, pk):
#     try:
#         address = Address.objects.get(pk=pk)
#     except Address.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = AddressSerializer(address)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = AddressSerializer(address,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         address.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

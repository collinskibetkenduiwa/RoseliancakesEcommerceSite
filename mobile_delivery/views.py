from rest_framework import routers, serializers, viewsets
from .serializers import DeliverySerializer
from .models import ClearOrders
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class DeliveryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ClearOrders.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAuthenticated]


    def post(self, request, format=None):
        serializer = DeliverySerializer(data=request.data, instance=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import viewsets
from rest_framework.response import Response
from .models import MenuItem, Order
from .serializers import MenuItemSerializer, OrderSerializer
from rest_framework.decorators import action

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        order = self.get_object()
        status = request.data.get('status', '')
        if status not in ['pending', 'completed']:
            return Response({"detail": "Invalid status"}, status=400)
        order.status = status
        order.save()
        return Response({'status': 'Order status updated'})


from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import MenuItemSerializer, BookingItemSerializer

from .models import menu, booking

# Create your views here.

def index(request):
    return render(request, 'index.html', {})
class MenuItemsView(generics.ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuItemSerializer
        

class BookingView(ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = BookingItemSerializer
    permission_classes = [IsAuthenticated]


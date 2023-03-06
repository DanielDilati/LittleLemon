from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Booking, MenuItems
from .serializers import BookingSerializer, MenuItemsSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.authtoken.models import Token


# Create your views here.

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer



class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer



class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer




def index(request):
    return render(request, 'index.html', {})

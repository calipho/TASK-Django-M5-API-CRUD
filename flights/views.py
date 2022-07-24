from datetime import datetime

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from .models import Booking, Flight
from .serializers import BookingListSerializer, FlightListSerializer, BookingDetailSerializer, BookingCreateSerializer, BookingUpdateSerializer, BookingDeleteSerializer


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = BookingListSerializer


class BookingDetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'

    def get_object(self):
        return Booking.objects.get(id=self.kwargs['booking_id'])


class UpdateBookingView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'


class CreateBookingView(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer


class DeleteBookingView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDeleteSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'

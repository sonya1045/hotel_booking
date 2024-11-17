from django.urls import path
from app_booking import views

urlpatterns = [
    path('rooms/', views.room_list, name = "room-list"),
    path('book-room/<int:pk>', views.booking_room, name = "book-room"),
    path('booking-details/<int:pk>', views.booking_details, name = "booking-details"),
    path('room-detail/<int:pk>', views.room_detail, name = "room-detail")


]

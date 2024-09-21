from django.contrib import admin
from django.urls import path
from app_booking import views

urlpatterns = [
    path('rooms/', views.room_list, name = "room_list"),
    path('book-room/', views.booking_room, name = "book-room"),
    path('booking-details/<int:pk>', views.booking_details, name = "booking-details")


]

from django.shortcuts import render, redirect
from .models import Room, Booking 
from django.http import HttpResponse

def room_list(request):
    if request.method == "POST":
        return redirect("room-detail", pk=Room.number)
    else:
        rooms = Room.objects.all()
        context = {
            "rooms": rooms,
        }
        return render(request, "booking/room_list.html", context)

def booking_room(request, pk):
    if request.method == "POST":
        start_time = request.POST.get("start-time")
        end_time = request.POST.get("end-time")
        room = Room.objects.get(number=pk)
        
        booking = Booking.objects.create(
            user = request.user,
            room = room,
            start_time = start_time,
            end_time = end_time
        )
        return redirect("booking-details", pk=booking.id)
    
    else:
        return render(request, template_name='booking/booking_form.html')
    
def booking_details(request, pk):
    booking = Booking.objects.get(id=pk)
    context = {
        'booking': booking
    }
    return render(request, "booking/booking-details.html", context)

def room_detail(request, pk):
    room = Room.objects.get(number=pk)
    context = {
        'rooms': room
    }
    return render(request, "booking/room_detail.html", context)
            

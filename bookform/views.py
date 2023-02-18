from django.shortcuts import render, redirect
from .forms import BookingForm


def book_form(request):
    form = BookingForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # Send email here
            form.send_email()
            return redirect('booking_thankyou')
    return render(request, 'bookform/bookform.html', {'form': form})


def booking_thankyou(request):
    return render(request, 'bookform/thankyou.html')
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    apartment_text = 'Flats, Shared Rooms, Duplex, Short, Long'
   # apartment_text = 'Test'
    context = { 'apartment_text': apartment_text}
    return render(request, "index.html", context = context)

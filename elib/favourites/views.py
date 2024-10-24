from django.shortcuts import render


def favourites(request):
    return render(request, 'favourites/favourites.html')

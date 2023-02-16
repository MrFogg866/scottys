from django.shortcuts import render

def social_media(request):
    return render(request, 'social_media/social_media.html')
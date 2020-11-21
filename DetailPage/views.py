from django.shortcuts import render

def welcomeScreen(request):
    return render(request, 'DetailPage/welcomescreen.html')
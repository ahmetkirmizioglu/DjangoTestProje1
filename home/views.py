from django.shortcuts import render
# from django.shortcuts import HttpResponse


# Create your views here.
def home_view(request):

    if request.user.is_authenticated:
        context = {
            'isim': 'user',

    }
    else:
        context = {
            'isim': 'quest',

    }
    return render(request, 'home.html', context)

from django.shortcuts import render

from mysteries.models import Mystery as MysteryModel

def index(request):
    mysteries_of_the_day = MysteryModel.get_mysteries_of_the_day()

    context = {
        'mysteries': mysteries_of_the_day
    }

    print(context)

    return render(request, 'pages/index.html', context=context)

from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipes(request, dish: str = None):
    if dish:
        if dish in DATA:
            servings = int(request.GET.get('servings', '1'))
            recipe = {key: value * servings for key, value in DATA[dish].items()}
        else:
            recipe = {}
        context = {'recipe': recipe}
        return render(request, 'calculator/index.html', context=context)
    else:
        return HttpResponse('<h2>бюдо не задано</h2>')

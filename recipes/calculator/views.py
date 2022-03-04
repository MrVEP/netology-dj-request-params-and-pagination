from django.shortcuts import render

DATA = {
    'omlet': {
        'title': 'Омлет',
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'title': 'Паста',
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'title': 'Бутерброд',
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def home_view(request):
    template_name = 'calculator/home.html'
    pages = {}
    for recipe in DATA:
        pages[DATA[recipe]['title']] = f'/{recipe}'
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def recipe_view(request, recipe):
    template_name = 'calculator/recipe.html'
    context = {
        'recipe': {

        }
    }
    servings = int(request.GET.get('servings'))
    for ingredient in DATA[recipe]:
        if ingredient != 'title':
            context['recipe'][ingredient] = DATA[recipe][ingredient] * servings
    return render(request, template_name, context)

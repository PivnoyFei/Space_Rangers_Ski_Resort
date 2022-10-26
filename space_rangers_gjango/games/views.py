from django.shortcuts import render

from games import messages
from ski_resort.models import Ski

dict_models = {'Лыжный курорт': Ski}


def index(request):
    context = {
        "user": request.user,
        "description": messages.game_description,
    }
    return render(request, "games/index.html", context)


def game(request):
    game_continue, description, complexity, name = True, False, False, False
    for key, values in messages.game_description.items():
        if request.POST.get(key):
            description = values[2] if len(values) == 3 else values[0]
            complexity = values[1]
            if dict_models[key].objects.filter(user=request.user).exists():
                game_continue = False
            name = key

    context = {
        "user": request.user,
        "name": name,
        "complexity": complexity,
        "description": description,
        "game_continue": game_continue,
        "start_game": messages.start_game
    }
    return render(request, "games/game.html", context)

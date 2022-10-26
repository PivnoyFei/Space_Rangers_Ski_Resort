from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ski_resort import messages, services, talk_services
from ski_resort.models import Ski


@login_required
def ski_start(request):
    ski = Ski.objects.filter(user=request.user)
    if ski.exists():
        ski[0].delete()
    game = Ski.objects.create(user=request.user)
    context = services.__context(
        game, messages.question_one, messages.start_text)
    return render(request, "ski_resort/ski.html", context)


@login_required
def ski_continue(request):
    game = Ski.objects.get(user=request.user)
    question = messages.question_one if game.day == 0 else messages.question
    start_text = (
        messages.start_text if game.day == 0 else talk_services.__days(game)
    )
    for i in messages.new_day:
        if request.POST.get(i) in messages.new_day:
            question, start_text = services.__new_day(game)

    context = services.__context(game, question, start_text)
    return render(request, "ski_resort/ski.html", context)


@login_required
def ask(request):
    game = Ski.objects.get(user=request.user)
    if game.day == 0:
        question = messages.ask_advisers_start
    else:
        question = messages.ask_advisers
    start_text = messages.question_2[0]

    for index, values in enumerate(messages.ask_advertising_manager_start):
        if request.POST.get(values):
            if index < 6:
                game.advertising = index * 10000
                game.save()
                context = services.__context(game, question, start_text)
                return render(request, "ski_resort/ask.html", context)
            if values in messages.new_day:
                return ski_continue(request)

    for index, values in enumerate(messages.ask_advisers_start):
        if request.POST.get(values):
            start_text = talk_services.__talk(
                game, messages.talk[index], values
            )
            if values == "Поговорить с менеджером по рекламе":
                if game.day == 0:
                    question = messages.ask_advertising_manager_start
                else:
                    question = messages.ask_advertising_manager

    context = services.__context(game, question, start_text)
    return render(request, "ski_resort/ask.html", context)


@login_required
def building(request):
    game = Ski.objects.get(user=request.user)
    question = messages.question_building
    start_text = messages.question_2[1]

    for index, values in enumerate(question):
        if request.POST.get(values):
            if index < 7:
                start_text = talk_services.__talk_building(game, index)
            if index == 7:
                return redirect("ski_resort:ski_continue")
            if values in messages.new_day:
                return ski_continue(request)

    context = services.__context(game, question, start_text)
    return render(request, "ski_resort/building.html", context)

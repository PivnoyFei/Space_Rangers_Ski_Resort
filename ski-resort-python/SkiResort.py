import random
import QuestTexts as Q
from ClassSkiResort import Day


def new_day(d):
    if d.day == 30:
        d.day = 0
        if d.month == 12:
            d.month = -1
        d.month += 1
    d.day += 1
    d.building = 0
    d.count_building = 0

    d.profit_newbie()
    d.profit_professional()
    d.cr += d.income_newbie + d.income_professional

    d.get_arrived_left_people()

    if d.day == 1:
        d.left_professional = 0
    d.people()
    d.old_professional = d.professional
    d.old_newbie = d.newbie

    d.get_arrived_left_newbie()
    d.get_arrived_left_professional()

    d.get_trail_maintenance()
    d.cr -= d.trail_maintenance
    d.cr -= d.advertising

    for _ in range(int(d.advertising / 10000)):
        d.popularity += random.randint(3, 5)
    d.popularity -= random.randint(5, 10)
    if d.popularity > 100:
        d.popularity = 100

    global START
    if d.popularity < 0:
        print(Q.the_end[2])
        return main(START)
    if d.day > 20 and START is False:
        print(Q.the_end[0])
        return main(START)
    if d.cr < 0:
        print(Q.the_end[1].format(name=name))
        return main(START)
    if d.cr > 1000000 and d.day <= 20 and START is False:
        if d.popularity > 60:
            d.popularity -= 40
        elif 60 > d.popularity > 40:
            d.popularity -= 20
        START = True
        print(Q.end_or[0].format(name=name))
        return main(d)
    if d.cr > 10000000:
        START = False
        print(Q.end_or[1].format(name=name))
        return main(START)

    print("========================================== НОВЫЙ ДЕНЬ ==========================================")
    n_day = random.randint(0, 2)
    if n_day == 2:
        d.cr -= 1000
    elif n_day == 3:
        d.popularity += random.randint(2, 4)
    print(Q.qwerty_break[n_day])
    return the_game(d)


def get_advertising(d):
    choice = 0
    num_choice = int(d.advertising / 10000)
    while choice not in (6, 7):
        count = 0
        if d.advertising == 0:
            for i in Q.qwerty_advertising:
                if count != 0:
                    print(i)
                count += 1
        else:
            for i in Q.qwerty_advertising:
                if count != num_choice:
                    print(i)
                count += 1

        choice = input()
        if choice.isdigit():
            choice = int(choice)

        if d.advertising != 0:
            print()
        if choice in (0, 1, 2, 3, 4, 5) and choice != num_choice:
            d.advertising = choice * 10000
            print(f"\nБудет сделано сказал менеджер по рекламе. "
                  f"- Текущие расходы на рекламу равны {d.advertising} cr в день. ")
            print()
        elif choice == 6:
            return talk(d)
        elif choice == 7:
            return new_day(d)
        num_choice = choice


def talk(d):
    d.profit_newbie()
    d.profit_professional()
    d.get_lift_occupancy()
    d.get_hotel_occupancy()
    d.get_track_occupancy_newbie()
    d.get_track_occupancy_professional()
    d.get_balance_for_tomorrow()

    advisors = {'cr': d.cr,
                'income': d.income_newbie + d.income_professional,
                'maintenance': d.trail_maintenance,
                'advertising': d.advertising,
                'building': d.building,
                'balance': d.balance_for_tomorrow,
                'people': d.newbie + d.professional,
                'newbie': d.newbie,
                'professional': d.professional,
                'hotel': d.hotel_occupancy,
                'restauran': d.restauran * Q.restauran[1],
                'lift': d.lift_occupancy,
                'track_newbie': d.track_occupancy_newbie,
                'track_professional': d.track_occupancy_professional,
                'popularity': d.popularity}

    your_choice = 0
    while your_choice not in (4, 5, 6):
        print(Q.qwerty_2[0], *Q.qwerty_3, sep="\n")
        if d.day != 0:
            print(Q.qwerty_3_1)

        your_choice = input()
        if your_choice.isdigit():
            your_choice = int(your_choice) - 1

        if your_choice in [0, 1, 2, 3, 4]:
            print(Q.talk[your_choice].format(**advisors))
            print()
            if your_choice == 4:
                return get_advertising(d)
        elif your_choice == 5:
            return new_day(d)
        elif d.day != 0 and your_choice == 6:
            return menu(d)


def get_building(d):
    choice_building = 0
    while choice_building != 7:
        print(Q.qwerty_2[1])

        choice_building = input(Q.qwerty_building)
        if choice_building.isdigit():
            choice_building = int(choice_building) - 1

        if choice_building < 7:
            count = d.cr - Q.company_list[choice_building][0]
            if d.count_building < 2 and count > 0:
                d.cr -= Q.company_list[choice_building][0]
                if choice_building == 0:
                    d.hotel += 1
                elif choice_building == 1:
                    d.restauran += 1
                elif choice_building == 2:
                    d.low_track += 1
                elif choice_building == 3:
                    d.middle_track += 1
                elif choice_building == 4:
                    d.high_track += 1
                elif choice_building == 5:
                    d.lift += 1
                elif choice_building == 6:
                    d.kupe_lift += 1
                d.building += Q.company_list[choice_building][0]
                d.count_building += 1
                d.popularity += random.randint(3, 5)
                print(Q.qwerty_4[choice_building])
            elif d.count_building == 2:
                print("\nВы не можете строить больше двух сооружений в день")
                return menu(d)
            elif count < 0:
                print("\nНедостаточно средств")
        elif choice_building == 7:
            return menu(d)
        elif choice_building == 8:
            return new_day(d)


def one_day(d):
    print(Q.start_text, *Q.qwerty_one, sep="\n")
    want_to_play = 0
    while want_to_play != 1 and want_to_play != 2:

        want_to_play = input()
        if want_to_play.isdigit():
            want_to_play = int(want_to_play)

        if want_to_play == 1:
            return talk(d)
        elif want_to_play == 2:
            return new_day(d)


def menu(d):
    print(*Q.qwerty, sep='\n')
    play = 0
    while play != 1 and play != 2 and play != 3:

        play = input()
        if play.isdigit():
            play = int(play)

        if play == 1:
            return talk(d)
        elif play == 2:
            return get_building(d)
        elif play == 3:
            return new_day(d)
        elif play.lower() in ["закончить", "завершить", "закрыть"]:
            break
        play = 0


def the_game(d):
    lift_places = (d.lift * Q.lift[1]) + (d.kupe_lift * Q.kupe_lift[1])
    hotel_places = d.hotel * Q.hotel[1]
    restauran_places = d.restauran * Q.restauran[1]
    track_occupancy_newbie = (d.low_track * Q.low_track[2]
                              + d.middle_track * Q.middle_track[2])
    track_occupancy_professional = (d.high_track * Q.high_track[2]
                                    + d.middle_track * Q.middle_track[2])
    if START is False:
        left_days = 20 - d.day
    else:
        left_days = d.day + d.month * 30
    days_list = {"day": d.day,
                 "month": Q.month[d.month],
                 "left_days": left_days,
                 "it_was_newbie": d.old_newbie,
                 "newbie_left": d.left_newbie,
                 "newbie_arrived": d.arrived_newbie,
                 "now_newbie": d.newbie,
                 "it_was_professional": d.old_professional,
                 "professional_left": d.left_professional,
                 "professional_arrived": d.arrived_professional,
                 "now_professional": d.professional,
                 "cr_newbie": d.income_newbie,
                 "cr_professional": d.income_professional,
                 "cr_track": d.trail_maintenance,
                 "cr_advertising": d.advertising,
                 "cr": d.cr,
                 "popularity": d.popularity,
                 "total_people": d.newbie + d.professional,
                 "hotel": d.hotel,
                 "hotel_places": hotel_places,
                 "restauran": d.restauran,
                 "restauran_places": restauran_places,
                 "lift_places": lift_places,
                 "track_newbie": track_occupancy_newbie,
                 "track_professional": track_occupancy_professional}
    if START is False:
        print(Q.days.format(**days_list))
    else:
        print(Q.days_end.format(**days_list))
    return menu(d)


def main(d):
    if d is False:
        d = Day()
        print(Q.beginning_of_the_game[0],
              Q.beginning_of_the_game[2])
    else:
        print(*Q.beginning_of_the_game)
    global START
    while True:
        want_to_play = input()
        if want_to_play.lower() in ["начать новую игру", "начать", "1"]:
            d = None
            d = Day()
            START = False
            one_day(d)
        elif want_to_play.lower() in ["продолжить", "2"] and START == True:
            START = True
            the_game(d)
        elif want_to_play.lower() in ["закончить", "завершить", "закрыть", "3"]:
            break



if __name__ == '__main__':
    name = 'Пивной Фей'
    START = False
    main(START)

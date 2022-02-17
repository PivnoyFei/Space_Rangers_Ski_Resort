import random
import QuestTexts as Q
from ClassSkiResort import D

def new_day():
    D.day += 1
    
    D.left_newbie = random.randint(3, 9)
    D.arrived_newbie = random.randint(7, 13)
    D.left_professional = random.randint(1, 3)
    D.arrived_professional = random.randint(2, 5)

    if D.day == 1:
        D.left_professional = 0

    if D.popularity < 30:
        D.left_newbie += random.randint(1, 2)
        D.arrived_newbie -= 1
        D.left_professional += 1
        D.arrived_professional -= 1
    elif D.popularity > 60:
        D.left_newbie -= 1
        D.arrived_newbie += random.randint(1, 3)
        D.left_professional -= 1
        D.arrived_professional += random.randint(1, 2)

    D.income_newbie = D.newbie * 2000
    D.income_professional = D.professional * 6000
    D.old_professional = D.professional
    D.old_newbie = D.newbie

    D.trail_maintenance = (D.low_track * Q.low_track[1]
                         + D.middle_track * Q.middle_track[1]
                         + D.high_track * Q.high_track[1])

    D.cr += D.income_newbie + D.income_professional

    D.newbie += D.arrived_newbie - D.left_newbie  # новичков приехало и уехало
    D.professional += D.arrived_professional - D.left_professional

    D.cr -= D.trail_maintenance
    D.cr -= D.advertising

    D.popularity += int((D.advertising / 10000) * random.randint(3, 5))
    D.popularity -= random.randint(5, 10)
    if D.popularity < 0 or D.cr < 0:
        print("Вы проиграли")
    print("================================================================")
    n_day = random.randint(0, 2)
    if n_day == 2:
        D.cr -= 1000
    print(Q.qwerty_break[n_day])
    return the_game()


def get_advertising():
    print(*Q.qwerty_advertising, sep="\n")
    choice = 0
    while choice not in (6, 7):
        choice = int(input())
        if choice in (1, 2, 3, 4, 5):
            D.advertising = int(choice * 10000)
            print(f"Окай мы будем тратить на рекламу {D.advertising}. "
                  f"Что нибудь еще?")
        elif choice == 6:
            return talk()
        elif choice == 7:
            return new_day()


def talk():
    lift_occupancy = D.kupe_lift * Q.kupe_lift[1] + D.lift * Q.lift[1]
    hotel_occupancy = (((D.hotel * Q.hotel[1]) / 100)
                       * (D.newbie + D.professional))
    track_occupancy_newbie = (D.low_track * Q.low_track[2]
                              + D.middle_track * Q.middle_track[2])
    track_occupancy_professional = (D.high_track * Q.high_track[2]
                                    + D.middle_track * Q.middle_track[2])
    balance_for_tomorrow = (D.cr + D.income_newbie
                            + D.income_professional
                            - D.building
                            - D.trail_maintenance
                            - D.advertising)
    advisors = {'cr': D.cr,
                'income': D.income_newbie + D.income_professional,
                'maintenance': D.trail_maintenance,
                'advertising': D.advertising,
                'building': D.building,
                'balance': balance_for_tomorrow,
                'people': D.newbie + D.professional,
                'newbie': D.newbie,
                'professional': D.professional,
                'hotel': hotel_occupancy,
                'restauran': D.restauran * Q.restauran[1],
                'lift': lift_occupancy,
                'track_newbie': track_occupancy_newbie,
                'track_professional': track_occupancy_professional,
                'popularity': D.popularity}

    your_choice = 0
    while your_choice not in (4, 5, 6):
        print(Q.qwerty_2[0], *Q.qwerty_3, sep="\n")
        if D.day != 0:
            print(Q.qwerty_3_1)
        your_choice = int(input()) - 1
        if your_choice in [0, 1, 2, 3, 4]:
            print(Q.talk[your_choice].format(**advisors))
            if your_choice == 4:
                return get_advertising()
        elif your_choice == 5:
            return new_day()
        elif D.day != 0 and your_choice == 6:
            return menu()


def get_building():
    choice_building = 0
    while choice_building != 7:
        print(Q.qwerty_2[1])
        choice_building = (int(input(Q.qwerty_building)) - 1)
        if choice_building in (0, 1, 2, 3, 4, 5, 6):
            count = D.cr - Q.company_list[choice_building][0]
            if D.count_building <= 2 and count > 0:
                D.cr -= Q.company_list[choice_building][0]
                if choice_building == 0:
                    D.hotel += 1
                elif choice_building == 1:
                    D.restauran += 1
                elif choice_building == 2:
                    D.low_track += 1
                elif choice_building == 3:
                    D.middle_track += 1
                elif choice_building == 4:
                    D.high_track += 1
                elif choice_building == 5:
                    D.lift += 1
                elif choice_building == 6:
                    D.kupe_lift += 1
                D.count_building += 1
            else:
                print("Недостаточно средств")
        elif choice_building == 7:
            return menu()


def one_day():
    print(Q.start_text, *Q.qwerty_one, sep="\n")
    want_to_play = 0
    while want_to_play != 1 and want_to_play != 2:
        want_to_play = int(input())
        if want_to_play == 1:
            return talk()
        elif want_to_play == 2:
            return new_day()


def menu():
    print(*Q.qwerty, sep='\n')
    play = 0
    while play != 1 and play != 2 and play != 3:
        play = int(input())
        if play == 1:
            return talk()
        elif play == 2:
            return get_building()
        elif play == 3:
            return new_day()
        play = 0


def the_game():
    lift_places = (D.lift * Q.lift[1]) + (D.kupe_lift * Q.kupe_lift[1])
    hotel_places = D.hotel * Q.hotel[1]
    restauran_places = D.restauran * Q.restauran[1]
    track_occupancy_newbie = (D.low_track * Q.low_track[2]
                              + D.middle_track * Q.middle_track[2])
    track_occupancy_professional = (D.high_track * Q.high_track[2]
                                    + D.middle_track * Q.middle_track[2])
    days_list = {"day": D.day,
                 "left_days": 20 - D.day,
                 "it_was_newbie": D.old_newbie,
                 "newbie_left": D.left_newbie,
                 "newbie_arrived": D.arrived_newbie,
                 "now_newbie": D.newbie,
                 "it_was_professional": D.old_professional,
                 "professional_left": D.left_professional,
                 "professional_arrived": D.arrived_professional,
                 "now_professional": D.professional,
                 "cr_newbie": D.income_newbie,
                 "cr_professional": D.income_professional,
                 "cr_track": D.trail_maintenance,
                 "cr_advertising": D.advertising,
                 "cr": D.cr,
                 "popularity": D.popularity,
                 "hotel": D.hotel,
                 "hotel_places": hotel_places,
                 "restauran": D.restauran,
                 "restauran_places": restauran_places,
                 "lift_places": lift_places,
                 "track_newbie": track_occupancy_newbie,
                 "track_professional": track_occupancy_professional}

    print(Q.days.format(**days_list))
    return menu()


while True:
    want_to_play = input(Q.beginning_of_the_game)
    if want_to_play.lower() in ["начать новую игру", "начать", "1"]:
        one_day()
    elif want_to_play.lower() in ["продолжить", "2"]:
        the_game()
    elif want_to_play.lower() in ["закончить", "завершить", "закрыть", "3"]:
        break


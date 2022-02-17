import QuestTexts as Q


class Day:
    cr = 100000  # деньги
    hotel = 1  # отель
    restauran = 1  # ресторан
    low_track = 1  # маленькая горка
    middle_track = 0  # средняя горка
    high_track = 0  # большая горка
    lift = 1  # подьемник
    kupe_lift = 0  # кабиночный подьемник
    newbie = 20  # новичек
    professional = 0  # профессионал
    advertising = 0  # расходы на рекламу
    popularity = 50  # Популярность курорта
    day = 0
    old_professional = 0
    old_newbie = 0
    wesd = 0

    left_newbie = 0  # Уехало новичков
    arrived_newbie = 0  # Приехало новичков
    left_professional = 0  # Уехало Профессионалов
    arrived_professional = 0  # Приехало Профессионалов

    income_newbie = newbie * 2000
    income_professional = 0
    building = 0
    trail_maintenance = 10000

    count_building = 0


D = Day()

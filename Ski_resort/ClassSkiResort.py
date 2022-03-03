import QuestTexts as Q
import random


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

    month = 0
    day = 0

    old_professional = 0
    old_newbie = 0
    wesd = 0

    left_newbie = 0  # Уехало новичков
    arrived_newbie = 0  # Приехало новичков
    left_professional = 0  # Уехало Профессионалов
    arrived_professional = 0  # Приехало Профессионалов

    income_newbie = 0
    income_professional = 0
    building = 0
    trail_maintenance = 10000

    count_building = 0

    lift_occupancy = None
    track_occupancy_professional = None
    hotel_occupancy = None
    track_occupancy_newbie = None
    balance_for_tomorrow = None

    def get_arrived_left_people(self):
        self.left_newbie = random.randint(3, 9)
        self.arrived_newbie = random.randint(7, 13)
        self.left_professional = random.randint(1, 3)
        self.arrived_professional = random.randint(2, 6)

        if self.popularity < 20:
            self.left_newbie += 1
            self.arrived_newbie -= 1
            self.arrived_professional -= 1

        if self.popularity < 30:
            self.left_newbie += 1
            self.arrived_newbie -= 1
            self.left_professional += 1
            self.arrived_professional -= 1

        elif self.popularity > 60:
            self.left_newbie -= 1
            self.arrived_newbie += random.randint(1, 3)
            self.left_professional -= 1
            self.arrived_professional += random.randint(1, 2)

        if self.popularity > 70:
            self.arrived_newbie += random.randint(1, 3)
            self.arrived_professional += random.randint(1, 3)

        if self.popularity > 85:
            self.arrived_newbie += random.randint(1, 3)
            self.arrived_professional += random.randint(2, 5)

        if self.popularity > 95:
            self.arrived_newbie += random.randint(2, 5)
            self.arrived_professional += random.randint(2, 7)

    def people(self):
        count = 0
        if self.hotel * Q.hotel[1] < self.newbie + self.professional:
            count += (self.newbie + self.professional) - self.hotel * Q.hotel[1]

        if self.restauran * Q.restauran[1] < self.newbie + self.professional:
            count += ((self.newbie + self.professional) - self.restauran * Q.restauran[1])

        if (self.lift * Q.lift[1] + self.kupe_lift * Q.kupe_lift[1]) < self.newbie + self.professional:
            count += ((self.newbie + self.professional) - (self.lift * Q.lift[1]
                                                           + self.kupe_lift * Q.kupe_lift[1]))

        if (self.low_track * Q.low_track[2] + self.middle_track * Q.middle_track[2]) < self.newbie:
            count_newbie = (self.newbie - (self.low_track * Q.low_track[2]
                                           + self.middle_track * Q.middle_track[2]))
            self.popularity -= count_newbie
            self.newbie -= count_newbie
            self.left_newbie += count_newbie

        if (self.high_track * Q.high_track[2] + self.middle_track * Q.middle_track[2]) < self.professional:
            count_newbie = (self.professional - (self.high_track * Q.high_track[2]
                                                 + self.middle_track * Q.middle_track[2]))
            self.popularity -= count_newbie * 2
            self.professional -= count_newbie
            self.left_professional += count_newbie

        self.newbie -= int(count / 2)
        self.professional -= int(count / 2)
        self.popularity -= int(count * 1.5)
        self.left_newbie += int(count / 2)
        self.left_professional += int(count / 2)
        if self.left_newbie > self.newbie:
            self.left_newbie = self.newbie
        if self.left_professional > self.professional:
            self.left_professional = self.professional
        if self.newbie < 0:
            self.newbie = 0
        if self.professional < 0:
            self.professional = 0

    def profit_newbie(self):
        self.income_newbie = self.newbie * 2000

    def profit_professional(self):
        self.income_professional = self.professional * 6000

    def get_trail_maintenance(self):
        self.trail_maintenance = (self.low_track * Q.low_track[1]
                                  + self.middle_track * Q.middle_track[1]
                                  + self.high_track * Q.high_track[1])

    def get_arrived_left_newbie(self):
        self.newbie += self.arrived_newbie - self.left_newbie

    def get_arrived_left_professional(self):
        self.professional += self.arrived_professional - self.left_professional

    def get_lift_occupancy(self):
        self.lift_occupancy = self.kupe_lift * Q.kupe_lift[1] + self.lift * Q.lift[1]

    def get_hotel_occupancy(self):
        self.hotel_occupancy = int((self.newbie + self.professional)
                                   * 100 / (self.hotel * Q.hotel[1]))

    def get_track_occupancy_newbie(self):
        self.track_occupancy_newbie = (self.low_track * Q.low_track[2]
                                       + self.middle_track * Q.middle_track[2])

    def get_track_occupancy_professional(self):
        self.track_occupancy_professional = (self.high_track * Q.high_track[2]
                                             + self.middle_track * Q.middle_track[2])

    def get_balance_for_tomorrow(self):
        self.profit_newbie()
        self.profit_professional()
        self.balance_for_tomorrow = (self.cr + self.income_newbie
                                     + self.income_professional
                                     - self.building
                                     - self.trail_maintenance
                                     - self.advertising)

d = Day()

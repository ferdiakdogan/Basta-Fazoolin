from datetime import time


class Menu():

    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "{} Menu, available between {}:00 - {}:00.".format(self.name.title(), self.start_time, self.end_time)

    def calculate_bill(self, purchased_items):
        total_bill = 0.00
        for item in purchased_items:
            total_bill += self.items[item]
        return total_bill


class Franchise:

    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return "The restaurant is located in {}.".format(self.address)

    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if time <= menu.end_time and time >= menu.start_time:
                available_menus.append(menu)
        return available_menus


items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch = Menu("brunch", items, time(hour=11).isoformat(timespec='hours'), time(hour=16).isoformat(timespec='hours'))

items2 = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird = Menu("early_bird", items2, time(hour=15).isoformat(timespec='hours'),
                  time(hour=18).isoformat(timespec='hours'))

items3 = {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner = Menu("dinner", items3, time(hour=17).isoformat(timespec='hours'), time(hour=23).isoformat(timespec='hours'))

items4 = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids = Menu("kids", items4, time(hour=11).isoformat(timespec='hours'), time(hour=21).isoformat(timespec='hours'))

# print(kids)

bill = brunch.calculate_bill(["pancakes", "home fries", "coffee"])

# print(bill)

# print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

# print(flagship_store)
# print(new_installment)

print(new_installment.available_menus(time(hour=12).isoformat(timespec='hours')))

print(new_installment.available_menus(time(hour=17).isoformat(timespec='hours')))









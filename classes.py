from enum import Enum
from collections import Counter

class Gender(Enum):
    FEMALE = "Female"
    MALE = "Male"
    NON_BINARY = "Non-binary"

class AlcoholType(Enum):
    NON_ALCOHOLIC = 0
    LOW_ALCOHOLIC = 1
    ALCOHOLIC = 2
    STRONG_ALCOHOLIC = 3

owners_of_lucky_numbers = []

class Guest:
    def __init__(self, id=0, name="", age=0, city="", phone_number="", gender=Gender, disliked_drinks=None, drink_limits=None, cocktail_limits=None):
        self.id = id
        self.name = name
        self.age = age
        self.city = city
        self.phone_number = phone_number
        self.gender = gender
        self.disliked_drinks = disliked_drinks

        self.drink_limits = drink_limits or {
            AlcoholType.NON_ALCOHOLIC: 0,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        }
        self.cocktail_limits = cocktail_limits or {
            AlcoholType.NON_ALCOHOLIC: 0,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        }

    def is_lucky_phone_number(self):
        seven_count = self.phone_number.count("7")
        if seven_count > 3:
            owners_of_lucky_numbers.append(self.name)
            return True
        return False

    def filter_drinks(self, drinks):
        filtered_drinks = [drink for drink in drinks if drink.name not in self.disliked_drinks]
        return sorted(filtered_drinks, key=lambda d: d.profit(), reverse=True)

    def get_drink_recommendations(self, drinks, cocktails):
        drink_recommendations = []
        cocktail_recommendations = []

        cocktail_counter = Counter()
        
        for cocktail in sorted(cocktails, key=lambda c: c.profit(), reverse=True):
            if any(drink.name in self.disliked_drinks for drink in cocktail.basic_drinks):
                continue
            
            cocktail_type = cocktail.alcohol_type()
            
            if cocktail_counter[cocktail_type] < self.cocktail_limits[cocktail_type]:
                cocktail_recommendations.append(cocktail)
                cocktail_counter[cocktail_type] += 1

        drink_counter = Counter()
        
        for drink in self.filter_drinks(drinks):
            drink_type = drink.alcohol_type()
            
            if drink_counter[drink_type] < self.drink_limits[drink_type]:
                drink_recommendations.append(drink)
                drink_counter[drink_type] += 1

        return drink_recommendations, cocktail_recommendations

class Party:
    def __init__(self, day, reason):
        self.day = day
        self.reason = reason
        self.guests = []

    def add_guests(self, guest):
        self.guests.append(guest)

    def find_average_age(self, gender):
        guests_ = [guest.age for guest in self.guests if guest.gender == gender]
        if guests_:
            return sum(guests_) / len(guests_)
        return None

    def sort_guests(self):
        self.guests.sort(key=lambda guest: guest.id)
        
    def calculate_drinks_needed(self, drinks, cocktails):
        drink_count = Counter()
        total_profit = 0

        for guest in self.guests:
            drinks_recommended, cocktails_recommended = guest.get_drink_recommendations(drinks, cocktails)

            for drink in drinks_recommended:
                drink_count[drink.name] += 1
                total_profit += drink.profit()

            for cocktail in cocktails_recommended:
                drink_count[cocktail.name] += 1
                total_profit += cocktail.profit()  # Використовуємо метод profit() для отримання прибутку

        return dict(drink_count), total_profit

    def __repr__(self):
        guest_names = ", ".join([guest.name for guest in self.guests])
        return f"Party on {self.day} for {self.reason} with guests: {guest_names}"

class BasicDrink:
    def __init__(self, name="", cost=0.0, price=0.0, volume=0.0, alcohol_percentage=0.0):
        self.name = name
        self.cost = cost
        self.price = price
        self.volume = volume
        self.alcohol_percentage = alcohol_percentage

    def alcohol_type(self):
        if self.alcohol_percentage == 0:
            return AlcoholType.NON_ALCOHOLIC
        elif 0 < self.alcohol_percentage < 12:
            return AlcoholType.LOW_ALCOHOLIC
        elif 12 <= self.alcohol_percentage < 30:
            return AlcoholType.ALCOHOLIC
        else:
            return AlcoholType.STRONG_ALCOHOLIC

    def profit(self):
        return self.price - self.cost

class Additional:
    def __init__(self, name='', cost=0.0):
        self.name = name
        self.cost = cost

class Cocktail:
    def __init__(self, name='', price=0.0):
        self.name = name
        self.price = price
        self.basic_drinks = {}
        self.additionals = []

    def add_basic_drinks(self, drink, volume):
        self.basic_drinks[drink] = volume

    def add_additionals(self, additional):
        self.additionals.append(additional)

    def alcohol_type(self):
        total_volume = sum(self.basic_drinks.values())
        weighted_alcohol_content = sum(
            drink.alcohol_percentage * volume for drink, volume in self.basic_drinks.items() if isinstance(drink, BasicDrink)
        )
        alcohol_content = weighted_alcohol_content / total_volume if total_volume else 0
        if alcohol_content == 0:
            return AlcoholType.NON_ALCOHOLIC
        elif 0 < alcohol_content < 13:
            return AlcoholType.LOW_ALCOHOLIC
        elif 13 <= alcohol_content < 30:
            return AlcoholType.ALCOHOLIC
        else:
            return AlcoholType.STRONG_ALCOHOLIC

    def profit(self):
        drink_cost = sum(drink.cost * volume for drink, volume in self.basic_drinks.items())
        additional_cost = sum(additional.cost for additional in self.additionals)
        total_cost = drink_cost + additional_cost
        return self.price - total_cost
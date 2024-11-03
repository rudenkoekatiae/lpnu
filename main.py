from classes import Gender, AlcoholType, Guest, Party, owners_of_lucky_numbers, BasicDrink, Additional, Cocktail
from collections import Counter

def main():
    coke = BasicDrink("Coke", 60, 150, 0.3, 0)
    water = BasicDrink("Water", 20, 50, 0.3, 0)
    lemonade = BasicDrink("Lemonade", 70, 150, 0.3, 0)
    tonic_water = BasicDrink("Tonic water", 70, 155, 0.3, 0)
    sprite = BasicDrink("Sprite", 70, 150, 0.3, 0)
    bourbon = BasicDrink("Bourbon", 800, 1500, 0.2, 40)
    rum = BasicDrink("Rum", 450, 850, 0.2, 35)
    vodka = BasicDrink("Vodka", 400, 720, 0.1, 40)
    jagermeister = BasicDrink("Jagermeister", 900, 2000, 0.25, 35)
    aperol = BasicDrink("Aperol", 540, 1300,0.3, 11)
    whiskey = BasicDrink("Whiskey", 860, 1750, 0.2, 40)
    baileys = BasicDrink("Baileys", 990, 1990, 0.3, 17)
    cognac = BasicDrink("Cognac", 920, 1720, 0.2, 40)
    sparkle_water = BasicDrink("Sparkle water", 25, 55, 0.3, 0)
    apple_juice = BasicDrink("Apple juice", 80, 200, 0.3, 0)
    orange_juice = BasicDrink("Orange juice", 80, 200, 0.3, 0)
    peach_juice = BasicDrink("Peach juice", 80, 200, 0.3, 0)
    grape_juice = BasicDrink("Grape juice", 80, 200, 0.3, 0)
    tequila = BasicDrink("Tequila", 770, 1500, 0.2, 37)
    gin = BasicDrink("Gin", 650, 1300, 0.2, 39)
    red_wine = BasicDrink("Red wine", 490, 760, 0.3, 16)
    rose_wine = BasicDrink("Rose wine", 490, 760, 0.3, 14)
    white_wine = BasicDrink("White wine", 490, 760, 0.3, 16)
    rose_sparkling_wine = BasicDrink("Rose sparkling wine", 490, 760, 0.3, 12)
    white_sparkling_wine = BasicDrink("White sparkling wine", 490, 760, 0.3, 14)
    beer = BasicDrink("Beer", 120, 300, 0.7, 7)
    zhyvchyk = BasicDrink("Zhyvchyk", 40, 150, 0.3, 0)

    lemon = Additional("Lemon", 5)
    ice = Additional("Ice", 5)
    orange = Additional("Orange", 5)
    caramel_syrup = Additional("Caramel syrup", 5)
    mint = Additional("Mint", 5)
    cinnamon = Additional("Cinnamon", 3)
    coconut = Additional("Coconut", 3)
    cucumber = Additional("Cucumber", 3)
    cocktails_cherry = Additional("Cocktails cherry", 15)
    lemon_fresh = Additional("Lemon fresh", 6)
    espresso = Additional("Espresso", 10)

    vodka_tonic = Cocktail("Vodka Tonic", 135)
    vodka_tonic.add_basic_drinks(vodka, 0.05)
    vodka_tonic.add_basic_drinks(tonic_water, 0.2)
    vodka_tonic.add_additionals(lemon_fresh)
    vodka_tonic.add_additionals(ice)
    
    devils_cave = Cocktail("Devil`s cave", 200)
    devils_cave.add_basic_drinks(vodka, 0.3)
    devils_cave.add_additionals(lemon_fresh)
    devils_cave.add_additionals(ice)
    devils_cave.add_additionals(mint)

    mermaid_tears = Cocktail("Mermaid tears", 190)
    mermaid_tears.add_basic_drinks(tequila, 0.2)
    mermaid_tears.add_basic_drinks(grape_juice, 0.2)
    mermaid_tears.add_additionals(coconut)
    mermaid_tears.add_additionals(ice)

    spring_garden = Cocktail("Spring garden", 210)
    spring_garden.add_basic_drinks(white_wine, 0.18)
    spring_garden.add_basic_drinks(grape_juice, 0.2)
    spring_garden.add_basic_drinks(apple_juice, 0.1)
    spring_garden.add_additionals(ice)

    bloody_cherry = Cocktail("Bloody cherry", 230)
    bloody_cherry.add_basic_drinks(red_wine, 0.25)
    bloody_cherry.add_additionals(espresso)
    bloody_cherry.add_additionals(cocktails_cherry)
    bloody_cherry.add_additionals(ice)

    mellow_breeze = Cocktail("Mellow Breeze", 180)
    mellow_breeze.add_basic_drinks(white_wine, 0.2)
    mellow_breeze.add_basic_drinks(lemonade, 0.15)
    mellow_breeze.add_basic_drinks(peach_juice, 0.15)
    mellow_breeze.add_additionals(ice)
    mellow_breeze.add_additionals(mint)

    spiced_tonic = Cocktail("Spiced Tonic", 220)
    spiced_tonic.add_basic_drinks(gin, 0.2)
    spiced_tonic.add_basic_drinks(tonic_water, 0.15)
    spiced_tonic.add_basic_drinks(lemon_fresh, 0.1)
    spiced_tonic.add_additionals(cinnamon)
    spiced_tonic.add_additionals(ice)

    sunny_rush = Cocktail("Sunny Rush", 200)
    sunny_rush.add_basic_drinks(vodka, 0.15)
    sunny_rush.add_basic_drinks(orange_juice, 0.2)
    sunny_rush.add_basic_drinks(sprite, 0.1)
    sunny_rush.add_additionals(orange)
    sunny_rush.add_additionals(caramel_syrup)

    chill_bliss = Cocktail("Chill Bliss", 160)
    chill_bliss.add_basic_drinks(aperol, 0.2)
    chill_bliss.add_basic_drinks(white_sparkling_wine, 0.25)
    chill_bliss.add_basic_drinks(sparkle_water, 0.1)
    chill_bliss.add_additionals(lemon)
    chill_bliss.add_additionals(mint)

    tropical_twist = Cocktail("Tropical Twist", 240)
    tropical_twist.add_basic_drinks(rum, 0.2)
    tropical_twist.add_basic_drinks(coke, 0.15)
    tropical_twist.add_basic_drinks(coconut, 0.05)
    tropical_twist.add_additionals(lemon)
    tropical_twist.add_additionals(ice)

    tropical_punch = Cocktail("Tropical Punch", 250)
    tropical_punch.add_basic_drinks(whiskey, 0.15)
    tropical_punch.add_basic_drinks(orange_juice, 0.2)
    tropical_punch.add_basic_drinks(peach_juice, 0.1)
    tropical_punch.add_additionals(cinnamon)
    tropical_punch.add_additionals(ice)

    berry_twist = Cocktail("Berry Twist", 210)
    berry_twist.add_basic_drinks(cognac, 0.15)
    berry_twist.add_basic_drinks(rose_wine, 0.2)
    berry_twist.add_basic_drinks(grape_juice, 0.1)
    berry_twist.add_additionals(cocktails_cherry)
    berry_twist.add_additionals(ice)

    espresso_bliss = Cocktail("Espresso Bliss", 230)
    espresso_bliss.add_basic_drinks(jagermeister, 0.2)
    espresso_bliss.add_basic_drinks(vodka, 0.1)
    espresso_bliss.add_additionals(espresso)
    espresso_bliss.add_additionals(caramel_syrup)
    espresso_bliss.add_additionals(ice)

    citrus_burst = Cocktail("Citrus Burst", 190)
    citrus_burst.add_basic_drinks(tequila, 0.15)
    citrus_burst.add_basic_drinks(lemonade, 0.2)
    citrus_burst.add_basic_drinks(lemon_fresh, 0.05)
    citrus_burst.add_additionals(lemon)
    citrus_burst.add_additionals(ice)

    island_dream = Cocktail("Island Dream", 250)
    island_dream.add_basic_drinks(bourbon, 0.15)
    island_dream.add_basic_drinks(sprite, 0.15)
    island_dream.add_basic_drinks(coconut, 0.05)
    island_dream.add_additionals(orange)
    island_dream.add_additionals(mint)

    creamy_harmony = Cocktail("Creamy Harmony", 200)
    creamy_harmony.add_basic_drinks(baileys, 0.2)
    creamy_harmony.add_basic_drinks(rum, 0.1)
    creamy_harmony.add_additionals(cinnamon)
    creamy_harmony.add_additionals(caramel_syrup)
    creamy_harmony.add_additionals(ice)

    refreshing_splash = Cocktail("Refreshing Splash", 140)
    refreshing_splash.add_basic_drinks(coke, 0.2)
    refreshing_splash.add_basic_drinks(lemonade, 0.2)
    refreshing_splash.add_additionals(ice)
    refreshing_splash.add_additionals(lemon)

    morning_boost = Cocktail("Morning Boost", 150)
    morning_boost.add_basic_drinks(zhyvchyk, 0.25)
    morning_boost.add_basic_drinks(peach_juice, 0.15)
    morning_boost.add_additionals(cucumber)
    morning_boost.add_additionals(mint)

    citrus_joy = Cocktail("Citrus Joy", 160)
    citrus_joy.add_basic_drinks(orange_juice, 0.25)
    citrus_joy.add_basic_drinks(tonic_water, 0.2)
    citrus_joy.add_additionals(ice)
    citrus_joy.add_additionals(lemon)

    berry_fizz = Cocktail("Berry Fizz", 160)
    berry_fizz.add_basic_drinks(grape_juice, 0.2)
    berry_fizz.add_basic_drinks(rose_sparkling_wine, 0.2)
    berry_fizz.add_additionals(cocktails_cherry)
    berry_fizz.add_additionals(mint)

    minty_green = Cocktail("Minty Green", 140)
    minty_green.add_basic_drinks(sprite, 0.2)
    minty_green.add_additionals(lemon_fresh)
    minty_green.add_additionals(mint)
    minty_green.add_additionals(ice)

    apple_beer_mix = Cocktail("Apple Beer Mix", 10)
    apple_beer_mix.add_basic_drinks(apple_juice, 0.2)
    apple_beer_mix.add_basic_drinks(beer, 0.3)

    playfulness = Cocktail("Playfulness", 185)
    playfulness.add_basic_drinks(jagermeister, 0.2)
    playfulness.add_basic_drinks(zhyvchyk, 0.2)
    playfulness.add_additionals(ice)
    playfulness.add_additionals(mint)
    playfulness.add_additionals(lemon_fresh)

    refreshing_citrus = Cocktail("Refreshing Citrus", 150)
    refreshing_citrus.add_basic_drinks(orange_juice, 0.25)
    refreshing_citrus.add_basic_drinks(lemonade, 0.25)
    refreshing_citrus.add_additionals(ice)
    refreshing_citrus.add_additionals(mint)

    tropical_fruit_fizz = Cocktail("Tropical Fruit Fizz", 160)
    tropical_fruit_fizz.add_basic_drinks(peach_juice, 0.2)
    tropical_fruit_fizz.add_basic_drinks(apple_juice, 0.2)
    tropical_fruit_fizz.add_basic_drinks(sparkle_water, 0.25)
    tropical_fruit_fizz.add_additionals(coconut)
    tropical_fruit_fizz.add_additionals(ice)

    berry_delight = Cocktail("Berry Delight", 140)
    berry_delight.add_basic_drinks(grape_juice, 0.25)
    berry_delight.add_basic_drinks(apple_juice, 0.2)
    berry_delight.add_basic_drinks(sprite, 0.2)
    berry_delight.add_additionals(cocktails_cherry)
    berry_delight.add_additionals(ice)

    peach_paradise = Cocktail("Peach Paradise", 130)
    peach_paradise.add_basic_drinks(peach_juice, 0.3)
    peach_paradise.add_basic_drinks(sparkle_water, 0.3)
    peach_paradise.add_additionals(lemon)
    peach_paradise.add_additionals(ice)



    katia = Guest(
        id=0, name="Katia", age=21, city="Lviv", phone_number="2102180507", gender=Gender.FEMALE,
        disliked_drinks=["Beer", "Cognac", "Bourbon"],
        drink_limits={
            AlcoholType.NON_ALCOHOLIC: 2,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 1
        },
        cocktail_limits={
            AlcoholType.NON_ALCOHOLIC: 3,
            AlcoholType.LOW_ALCOHOLIC: 1,
            AlcoholType.ALCOHOLIC: 2,
            AlcoholType.STRONG_ALCOHOLIC: 2
        }
    )
    victoria = Guest(
        id=1, name="Victoria", age=19, city="Lviv", phone_number="12347777", gender=Gender.FEMALE,
        disliked_drinks=["Beer", "Tequila", "Apple juice"],
        drink_limits={
            AlcoholType.NON_ALCOHOLIC: 2,
            AlcoholType.LOW_ALCOHOLIC: 1,
            AlcoholType.ALCOHOLIC: 2,
            AlcoholType.STRONG_ALCOHOLIC: 1
        },
        cocktail_limits={
            AlcoholType.NON_ALCOHOLIC: 1,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 1,
            AlcoholType.STRONG_ALCOHOLIC: 2
        }
    )
    andriy = Guest(
        id=2, name="Andriy", age=20, city="Kyiv", phone_number="12345678", gender=Gender.MALE,
        disliked_drinks=["Vodka", "Rum"],
        drink_limits={
            AlcoholType.NON_ALCOHOLIC: 2,
            AlcoholType.LOW_ALCOHOLIC: 1,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        },
        cocktail_limits={
            AlcoholType.NON_ALCOHOLIC: 3,
            AlcoholType.LOW_ALCOHOLIC: 2,
            AlcoholType.ALCOHOLIC: 2,
            AlcoholType.STRONG_ALCOHOLIC: 2
        }
    )
    adam = Guest(
        id=3, name="Adam", age=20, city="NYC", phone_number="0258631468", gender=Gender.MALE,
        disliked_drinks=["Vodka", "Rum"],
        drink_limits={
            AlcoholType.NON_ALCOHOLIC: 4,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 1,
            AlcoholType.STRONG_ALCOHOLIC: 2
        },
        cocktail_limits={
            AlcoholType.NON_ALCOHOLIC: 1,
            AlcoholType.LOW_ALCOHOLIC: 3,
            AlcoholType.ALCOHOLIC: 2,
            AlcoholType.STRONG_ALCOHOLIC: 2
        }
    )  

    jung_ho = Guest(
        id=4, name="Jung Ho", age=18, city="Seoul", phone_number="6158631452", gender=Gender.NON_BINARY,
        disliked_drinks=["Zhyvchyk", "Rum"],
        drink_limits={
            AlcoholType.NON_ALCOHOLIC: 2,
            AlcoholType.LOW_ALCOHOLIC: 1,
            AlcoholType.ALCOHOLIC: 1,
            AlcoholType.STRONG_ALCOHOLIC: 0
        },
        cocktail_limits={
            AlcoholType.NON_ALCOHOLIC: 2,
            AlcoholType.LOW_ALCOHOLIC: 2,
            AlcoholType.ALCOHOLIC: 1,
            AlcoholType.STRONG_ALCOHOLIC: 0
        }
    )

    sophia = Guest(
        5, "Sophia", 16, "NYC", "9877765420", Gender.FEMALE,
        disliked_drinks=["Coke", "Lemonade",],
        drink_limits={
            AlcoholType.NON_ALCOHOLIC: 9,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        },
        cocktail_limits={
            AlcoholType.NON_ALCOHOLIC: 0,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        }
    )
    
    charlie = Guest(
        6, "Charlie", 20, "Kyiv", "1111111111", Gender.NON_BINARY,
        disliked_drinks=["Jagermeister", "Aperol", "Whiskey"],
        drink_limits={
            AlcoholType.NON_ALCOHOLIC: 2,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 2,
            AlcoholType.STRONG_ALCOHOLIC: 1
        },
        cocktail_limits={
            AlcoholType.NON_ALCOHOLIC: 0,
            AlcoholType.LOW_ALCOHOLIC: 2,
            AlcoholType.ALCOHOLIC: 1,
            AlcoholType.STRONG_ALCOHOLIC: 0
        }
    )
    alex = Guest(
        7, "Alex", 26, "Florence", "7771112102", Gender.NON_BINARY,
        disliked_drinks=["Peach juice", "Rose wine"],
        drink_limits={
            AlcoholType.NON_ALCOHOLIC: 1,
            AlcoholType.LOW_ALCOHOLIC: 1,
            AlcoholType.ALCOHOLIC: 2,
            AlcoholType.STRONG_ALCOHOLIC: 0
        },
        cocktail_limits={
            AlcoholType.NON_ALCOHOLIC: 0,
            AlcoholType.LOW_ALCOHOLIC: 1,
            AlcoholType.ALCOHOLIC: 1,
            AlcoholType.STRONG_ALCOHOLIC: 1
        }
    )
    hae_soo = Guest(
        8, "Hae Soo", 17, "Seoul", "9568451230", Gender.MALE, 
        disliked_drinks=["Orange juice", "Sparkling water"],
        drink_limits={
            AlcoholType.NON_ALCOHOLIC: 3,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        },
        cocktail_limits={
            AlcoholType.NON_ALCOHOLIC: 2,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        }
    )  

    stacy = Guest(
        9, "Stacy", 15, "Paris", "1237890456", Gender.FEMALE,
        disliked_drinks=["Zhyvchyk", "Peach juice"],
        drink_limits={
            AlcoholType.NON_ALCOHOLIC: 2,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        },
        cocktail_limits={
            AlcoholType.NON_ALCOHOLIC: 4,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        }
    )

    elizabeth = Guest(
        10, "Elizabeth", 19, "London", "7771112102", Gender.FEMALE,
        disliked_drinks=["Red wine", "Rose sparkling wine", "White sparkling wine"],
        drink_limits={
            AlcoholType.NON_ALCOHOLIC: 2,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 2
        },
        cocktail_limits={
            AlcoholType.NON_ALCOHOLIC: 1,
            AlcoholType.LOW_ALCOHOLIC: 2,
            AlcoholType.ALCOHOLIC: 1,
            AlcoholType.STRONG_ALCOHOLIC: 0
        }
    )
    mia = Guest(
        id=11, name="Mia", age=19, city="Lviv", phone_number="12347777", gender=Gender.FEMALE,
        disliked_drinks=["Beer", "Tequila", "Apple juice"],
        drink_limits={
            AlcoholType.NON_ALCOHOLIC: 3,
            AlcoholType.LOW_ALCOHOLIC: 3,
            AlcoholType.ALCOHOLIC: 2,
            AlcoholType.STRONG_ALCOHOLIC: 2
        },
        cocktail_limits={
            AlcoholType.NON_ALCOHOLIC: 0,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        }
    )
    ava = Guest(
        12, "Ava", 15, "Paris", "1020304050", Gender.FEMALE,
        disliked_drinks=["Water", "Sprite"],
        drink_limits={
            AlcoholType.NON_ALCOHOLIC: 7,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        },
        cocktail_limits={
            AlcoholType.NON_ALCOHOLIC: 2,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        }
    )
    henry = Guest(
        13, "Henry", 17, "Lviv", "8070904060", Gender.MALE,
        disliked_drinks=["Sprite", "Orange juice"],
        drink_limits={
            AlcoholType.NON_ALCOHOLIC: 3,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        },
        cocktail_limits={
            AlcoholType.NON_ALCOHOLIC: 1,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        }
    )  

    riley = Guest(
        14, "Riley", 16, "Lviv", "1222222222", Gender.NON_BINARY,
        disliked_drinks=["Zhyvchyk", "Tonic water", "Lemonade"],
        drink_limits={
            AlcoholType.NON_ALCOHOLIC: 4,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        },
        cocktail_limits={
            AlcoholType.NON_ALCOHOLIC: 3,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        }
    )

    will = Guest(
        15, "Will", 27, "Madrid", "8888552233", Gender.MALE,
        disliked_drinks=["Coke", "Vodka",],
        drink_limits={
            AlcoholType.NON_ALCOHOLIC: 0,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        },
        cocktail_limits={
            AlcoholType.NON_ALCOHOLIC: 2,
            AlcoholType.LOW_ALCOHOLIC: 2,
            AlcoholType.ALCOHOLIC: 2,
            AlcoholType.STRONG_ALCOHOLIC: 2
        }
    )
    
    olivia = Guest(
        16, "Olivia", 24, "London", "1063788573", Gender.FEMALE,
        disliked_drinks=["Jagermeister", "Aperol", "Whiskey"],
        drink_limits={
            AlcoholType.NON_ALCOHOLIC: 2,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 2,
            AlcoholType.STRONG_ALCOHOLIC: 1
        },
        cocktail_limits={
            AlcoholType.NON_ALCOHOLIC: 1,
            AlcoholType.LOW_ALCOHOLIC: 2,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        }
    )
    dany = Guest(
        17, "Dany", 16, "NYC", "9877765425", Gender.FEMALE,
        disliked_drinks=["Peach juice", "Tonic water"],
        drink_limits={
            AlcoholType.NON_ALCOHOLIC: 4,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        },
        cocktail_limits={
            AlcoholType.NON_ALCOHOLIC: 2,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        }
    )
    taylor = Guest(
        18, "Taylor", 26, "Florence", "4567823665", Gender.NON_BINARY, 
        disliked_drinks=["Orange juice", "Sparkling water"],
        drink_limits={
            AlcoholType.NON_ALCOHOLIC: 0,
            AlcoholType.LOW_ALCOHOLIC: 1,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 2
        },
        cocktail_limits={
            AlcoholType.NON_ALCOHOLIC: 1,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 4
        }
    )  

    o_jun = Guest(
        19, "O jun", 17, "Seoul", "7373494773", Gender.NON_BINARY,
        disliked_drinks=["Lemonade", "Peach juice"],
        drink_limits={
            AlcoholType.NON_ALCOHOLIC: 2,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        },
        cocktail_limits={
            AlcoholType.NON_ALCOHOLIC: 3,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 0,
            AlcoholType.STRONG_ALCOHOLIC: 0
        }
    )

    olha = Guest(
        20, "Olha", 27, "Lviv", "0258461368", Gender.FEMALE,
        disliked_drinks=["Red wine", "Zhyvchyk"],
        drink_limits={
            AlcoholType.NON_ALCOHOLIC: 1,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 3,
            AlcoholType.STRONG_ALCOHOLIC: 0
        },
        cocktail_limits={
            AlcoholType.NON_ALCOHOLIC: 0,
            AlcoholType.LOW_ALCOHOLIC: 0,
            AlcoholType.ALCOHOLIC: 3,
            AlcoholType.STRONG_ALCOHOLIC: 0
        }
    )

    guests = [
        victoria, adam, jung_ho, katia, andriy, sophia, charlie, alex, hae_soo, stacy, elizabeth, ava,
        henry, riley, will, olivia, mia, taylor, o_jun, dany, olha
    ]

    drinks = [
        coke, water, lemonade, tonic_water, sprite, bourbon, rum,
        vodka, jagermeister, aperol, whiskey, baileys, cognac,
        sparkle_water, apple_juice, orange_juice, peach_juice, grape_juice,
        tequila, gin, red_wine, rose_wine, white_wine, rose_sparkling_wine, white_sparkling_wine,
        beer, zhyvchyk
    ]  
    cocktails = [
        vodka_tonic, vodka_tonic, devils_cave, mermaid_tears, spring_garden, bloody_cherry, mellow_breeze,
        spiced_tonic, sunny_rush, chill_bliss, tropical_twist, tropical_punch, berry_twist,
        espresso_bliss, citrus_burst, island_dream, creamy_harmony, refreshing_splash,
        morning_boost, citrus_joy, berry_fizz, minty_green, apple_beer_mix, playfulness, refreshing_citrus, tropical_fruit_fizz,
        berry_delight, peach_paradise
    ]
 


    new_year_party = Party("31/12/2024", "New Year")
    helloween_party_in_lviv = Party("31/10/2024", "Helloween in Lviv")

    def add_adult_guests_to_party(party, guests):
        for guest in guests:
            if guest.age >= 18:
                party.add_guests(guest)

    def add_lviv_guests_to_party(party, guests):
        for guest in guests:
            if guest.city =="Lviv":
                party.add_guests(guest)

    add_adult_guests_to_party(new_year_party, guests)
    add_lviv_guests_to_party(helloween_party_in_lviv, guests)

    print(new_year_party)
    print(helloween_party_in_lviv)

    print("Average age of male guests in New Year party:", new_year_party.find_average_age(Gender.MALE))
    print("Average age of female guests in New Year party:", new_year_party.find_average_age(Gender.FEMALE))
    print("Average age of non-binary guests in New Year party:", new_year_party.find_average_age(Gender.NON_BINARY))

    print("Average age of male guests in Lviv party:", helloween_party_in_lviv.find_average_age(Gender.MALE))
    print("Average age of female guests in Lviv party:", helloween_party_in_lviv.find_average_age(Gender.FEMALE))
    print("Average age of non-binary guests in Lviv party:", helloween_party_in_lviv.find_average_age(Gender.NON_BINARY))
    

    for guest in guests:
        guest.is_lucky_phone_number()

    new_year_party.sort_guests()
    helloween_party_in_lviv.sort_guests()

    print(f"Owners of lucky numbers: {owners_of_lucky_numbers}")

    drink_count = Counter()

    for guest in guests:
        drinks_recommended, cocktails_recommended = guest.get_drink_recommendations(drinks, cocktails)

        for drink in drinks_recommended:
            drink_count[drink.name] += 1

        for cocktail in cocktails_recommended:
            drink_count[cocktail.name] += 1

        print(f"Recommendations for {guest.name}:")
        print("  Drinks:" , [drink.name for drink in drinks_recommended])
        print("  Cocktails:", [cocktail.name for cocktail in cocktails_recommended])
        print()

    drinks_needed_new_year, total_profit_new_year = new_year_party.calculate_drinks_needed(drinks, cocktails)
    drinks_needed_helloween, total_profit_helloween = helloween_party_in_lviv.calculate_drinks_needed(drinks, cocktails)

    print("Total drinks needed for New Year party:", drinks_needed_new_year)
    print("Total profit from New Year party:", round(total_profit_new_year, 2))

    print("Total drinks needed for Halloween party in Lviv:", drinks_needed_helloween)
    print("Total profit from Halloween party in Lviv:", round(total_profit_helloween, 2))
    total_profit = total_profit_helloween + total_profit_new_year
    print("Total profit from parties:", round(total_profit, 2))

if __name__ == '__main__':
    main()

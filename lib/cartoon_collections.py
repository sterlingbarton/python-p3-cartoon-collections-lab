CHEESES = ["camembert", "gouda", "cheddar"]


def roll_call_dwarves(names):
    index = 1
    for name in names:
        print(f"{index}. {name}")
        index += 1


def summon_captain_planet(list):
    new_list = [f"{name.title()}!" for name in list]
    return new_list


def long_planeteer_calls(list):
    for name in list:
        if (len(name) > 4):
            return True

    return False


def find_the_cheese(foods):
    for food in foods:
        if food in CHEESES:
            return food

    return None

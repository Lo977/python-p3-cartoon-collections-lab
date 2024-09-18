def roll_call_dwarves(dwarfs):
    i = 1
    for dwarf  in dwarfs:
        print(f"{i}. {dwarf}")
        i += 1

def summon_captain_planet(planeteer_calls):
    calls = []
    for call in planeteer_calls:
        calls.append(call.capitalize() + "!")
    return calls

def long_planeteer_calls(long_calls):
    for sort_call in long_calls:
        if len(sort_call) > 4:
            return True
    return False

def find_the_cheese(foods):
    cheeses = ["camembert", "gouda", "cheddar"]

    for food in foods:
        if food in cheeses:
            return food
    return None

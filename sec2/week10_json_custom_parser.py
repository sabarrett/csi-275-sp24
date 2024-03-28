import json


class Pokemon:
    def __init__(self, name, level, hp, ability_scores=None):
        self.name = name
        self.level = level
        self.hp = 10 + (2 * level) if hp is None else hp
        self.ability_scores = {
            "attack": 11, "defense": 12, "spec. attack": 10,
            "spec. defense": 16, "speed": 14
        } if ability_scores is None else ability_scores


def encode_pokemon(p):
    if isinstance(p, Pokemon):
        return [p.name, p.level, p.hp, p.ability_scores]
    else:
        type_name = p.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' "
                        f"is not JSON serializable")


def encode_pokemon_enhanced(p):
    if isinstance(p, Pokemon):
        return {"__pokemon__": "true", "name": p.name, "level": p.level,
                "hp": p.hp, "ability_scores": p.ability_scores}
    else:
        type_name = p.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' "
                        f"is not JSON serializable")


def decode_pokemon(dct):
    if "__pokemon__" in dct:
        return Pokemon(dct["name"], dct["level"], dct["hp"],
                       dct["ability_scores"])
    return dct


pocket_monster = Pokemon("Swampert", 70, 238, {"attack": 190,
                                               "defense": 150,
                                               "spec. attack": 159,
                                               "spec. defense": 140,
                                               "speed": 118})

# Print out the object
print(pocket_monster)

# Can we encode it?
try:
    # pm_data = json.dumps(pocket_monster)
    # pm_data = json.dumps(pocket_monster, default=encode_pokemon)
    pm_data = json.dumps(pocket_monster, default=encode_pokemon_enhanced)
    print("Serializable!")

    # Can we decode it?
    # pm_decoded = json.loads(pm_data)
    pm_decoded = json.loads(pm_data, object_hook=decode_pokemon)
    print(pm_decoded)
    print(pm_decoded.level)
except TypeError:
    print("Nope, not serializable.")

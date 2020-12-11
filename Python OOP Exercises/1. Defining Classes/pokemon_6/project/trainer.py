# from pokemon_6.project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = list()

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            return "This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        for p in self.pokemon:
            if pokemon_name == p.name:
                self.pokemon.remove(p)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        first_line = f"Pokemon Trainer {self.name}\n"
        second_line = f"Pokemon count {len(self.pokemon)}\n"
        last_text = ""
        for p in self.pokemon:
            last_text += f'- {p.pokemon_details()}\n'
        return first_line + second_line + last_text

#
# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())

# Classes and Objects
# Author: Rachel
# 11 December 2025
import random


class Pokemon:
    def __init__(self):
        """Constructor"""
        self.name = ""
        self.species = ""
        self.type = "normal"
        self.level = 1
        self.age = 0
        if random.randint(0, 4096):
            self.is_shiny = False
        else:
            self.is_shiny = True
            print("This pokemn is shiny!✨")
        print("A pokemon is born!!")

    def talk(self):
        """Hear what the pokemo has to say
        the pokemon says its species name"""
        print(f'{self.name} says, "{self.species}".')

    def stats(self):
        """Display the stats of your pokemon"""
        print(f"---({self.species})---")
        print(f"    Name: {self.name}")
        print(f"    Type: {self.type}")
        print(f"    Age: {self.age}")
        print(f"    Level: {self.level}")
        print(" -----------------------")

    def dance(self):
        """Make the pokemon dance"""
        print(f"{self.name} uses rain dance, boosting water type moves.")


class Squirtle(Pokemon):
    def __init__(self):
        # call the constructor of pokemon
        super().__init__()
        self.name = "Squirtle"
        self.species = "Squirtle"
        self.type = "Water"

    def water_gun(self):
        """squirtle shoots water out of its mouth"""
        print(f"{self.name} used water gun!")


class Gengar(Pokemon):
    def __init__(self):
        super().__init__()
        self.name = "gengar"
        self.species = "gegar"
        self.type = "Ghost", "Poison"

    def shadow_sneak(self):
        """Gengar extends its shadow and attacks from behind"""
        print(f"{self.name} uses shadow sneak......")


if __name__ == "__main__":
    # Create a pokemon object
    pokemon_one = Pokemon()
    # Accss the pokemon's properties
    print("Pokemon name: ", pokemon_one.name)
    # Change the properties
    pokemon_one.name = "Gary"
    pokemon_one.species = "Pikachu"
    print("Pokemon name: ", pokemon_one.name)
    # Create another pokemon object
    pokemon_two = Pokemon()
    pokemon_two.name = "Pikachu"
    pokemon_two.species = "Pikachu"
    # Check to see if a value is a pokemon
    if pokemon_one == pokemon_two:
        print("They're the same.")
    else:
        print("They're individual pokemon.")

    if type(pokemon_one) is Pokemon:
        print(f"{pokemon_one.name} is a Pokemon")

    # Tell our pokemon to talk
    pokemon_one.talk()
    pokemon_two.talk()
    # display sttats of pokemo 1
    pokemon_one.stats()
    pokemon_one.dance()

    gengar_one = Gengar()
    squirtle_one = Squirtle()
    # use .water gun
    squirtle_one.water_gun()
    # use .talk
    squirtle_one.talk()

    gengar_one.talk()
    gengar_one.shadow_sneak()

class Pokemon(object):
    def __init__(self, name, type, effectiveAgainst):
        self.name = name
        self.type = type
        self.effectiveAgainst = effectiveAgainst
    def isEffectiveAgainst(self, anotherPokemon):
        return self.effectiveAgainst == anotherPokemon.type

def initializePokemons():
        pokemon = []
        pokemon.append(Pokemon("Balbasaur", "leaf", "water"))
        pokemon.append(Pokemon("Pikatchu", "electric", "water"))
        pokemon.append(Pokemon("Charizard", "fire", "leaf"))
        pokemon.append(Pokemon("Balbasaur", "water", "fire"))
        pokemon.append(Pokemon("Kingler", "water", "fire"))
        return pokemon

pokemon = initializePokemons()
wildPokemon = Pokemon("Oddish", "leaf", "water")
for i in range(len(pokemon)):
    if pokemon[i].isEffectiveAgainst(wildPokemon):
        a = pokemon[i].name
print("I choose you, "+a)
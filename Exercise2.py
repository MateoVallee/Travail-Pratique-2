#Fichier CSV :
import csv


#Creation du fichier et son contenu :
contenu = [
    ["Pikachu", 35, 55, 30, 50, 40, 90],
    ["Charizard", 78, 84, 78, 109, 85, 100],
    ["Magikarp", 20, 10, 55, 15, 20, 80]
]

with open("pokemon.csv", mode='w', newline='') as f_pokemon:
    pokemon_writer = csv.writer(f_pokemon)
    for pokemon in contenu:
        pokemon_writer.writerow(pokemon)


#CrÃ©ation d'une fonction pour pouvoir charger le contenu du fichier :
def charger_pokemons_csv(nom_fichier):
    pokemons = {}
    with open(nom_fichier, newline='') as f_pokemon:
        lecteur_csv = csv.reader(f_pokemon)
        for ligne in lecteur_csv:
            nom_pokemon = ligne[0]
            stats = [int(stat) for stat in ligne[1:]]
            pokemons[nom_pokemon] = stats
    return pokemons


#Exemple :
pkmn = charger_pokemons_csv("pokemon.csv")
for nom, stats in pkmn.items():
    print(f"{nom}: {stats}")

pkmn = charger_pokemons_csv("pokemon.csv")
print(isinstance(pkmn, dict))
print(isinstance(pkmn["Pikachu"], list))
print(isinstance(pkmn["Pikachu"][0], int))
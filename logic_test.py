"""
Part 1- Logic Excersice
a. numbers multiplies
b. pokemon subsequent names
"""
import numpy as np
import pandas as pd


def numbers_multiplies():
    """
    - Prints numbers from 0 to 100
    - Prints buzz in same line when number is even
    - Prints bazz in same line when number is a multiple of 5
    """
    numbers_array = np.arange(0, 101)
    for number in numbers_array:
        if(np.mod(number, 10) == 0):
            # Multiples of 10 are the common multiplies of 2 and 5.
            print(number, " buzz  bazz")
        elif(np.mod(number, 5) == 0):
            print(number, " bazz")
        elif(np.mod(number, 2) == 0):
            print(number, " buzz")
        else:
            print(number)


def next_pokemon(last_char, leftovers):
    thereIsNext = True
    while thereIsNext:
        for index, value in leftovers.items():
            isEmpty = (not leftovers[leftovers.str.startswith(
                last_char)].first_valid_index())
            isCero = (leftovers[leftovers.str.startswith(
                last_char)].first_valid_index() != 0)
            if isEmpty and isCero:
                thereIsNext = False
                break
            last_item_index = leftovers[leftovers.str.startswith(
                last_char)].first_valid_index()
            last_item = leftovers.loc[last_item_index]
            last_char = last_item[-1]
            leftovers = leftovers.drop(last_item_index)
            yield last_item


def pokemon_subsequent_names():
    """
    prints a sequence of pokemon names where:
    - the subsequent name of each pokemon starts with the final letter of the preceding name.
    - It has the highest number of elements fulfilling the above condition
    """
    pokemon_list = ['audino', 'bagon', 'baltoy', 'banette', 'bidoof', 'braviary', 'bronzor', 'carracosta', 'charmeleon', 'cresselia', 'croagunk', 'darmanitan', 'deino', 'emboar', 'emolga', 'exeggcute', 'gabite', 'girafarig', 'gulpin', 'haxorus', 'heatmor', 'heatran', 'ivysaur', 'jellicent', 'jumpluff', 'kangaskhan', 'kricketune', 'landorus', 'ledyba', 'loudred', 'lumineon', 'lunatone', 'machamp', 'magnezone',
                    'mamoswine', 'nosepass', 'petilil', 'pidgeotto', 'pikachu', 'pinsir', 'poliwrath', 'poochyena', 'porygon2', 'porygonz', 'registeel', 'relicanth', 'remoraid', 'rufflet', 'sableye', 'scolipede', 'scrafty', 'seaking', 'sealeo', 'silcoon', 'simisear', 'snivy', 'snorlax', 'spoink', 'starly', 'tirtouga', 'trapinch', 'treecko', 'tyrogue', 'vigoroth', 'vulpix', 'wailord', 'wartortle', 'whismur', 'wingull', 'yamask']
    current_sequence = []
    longest_sequence = []
    for index, pokemon in enumerate(pokemon_list):
        temporal_pokemon_list = pokemon_list[:]
        first_item = temporal_pokemon_list.pop(index)
        current_sequence.append(first_item)
        last_char = first_item[-1]
        pokemon_series = pd.Series(temporal_pokemon_list)
        for item in next_pokemon(last_char, pokemon_series):
            current_sequence.append(item)
        if len(current_sequence) > len(longest_sequence):
            longest_sequence = current_sequence
        current_sequence = []
    print(longest_sequence)


if __name__ == "__main__":
    numbers_multiplies()
    pokemon_subsequent_names()

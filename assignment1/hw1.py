#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import re
import numpy as np


def histogram_times(filename):
    csv_file = open(filename)
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    output = []
    for i in range(0, 24):
        output.append(0)
    for row in csv_reader:
        date, time, location, operator, flight_number, route, typ,\
            registration, cn_ln, aboard, fatalities, ground, summary = row
        if time and re.search(r'[0-9][0-9]:', time):
            value = re.search(r'[0-9][0-9]', time)
            output[int(value.group())] += 1
    csv_file.close()


def weigh_pokemons(filename, weight):
    json_file = open(filename, "r", encoding="utf-8")
    pokedex = json.load(json_file)
    json_file.close()
    pokemons = []
    for pokemon in pokedex["pokemon"]:
        p_weight = re.search(r'(\d+)\.(\d+)', pokemon["weight"])
        if float(p_weight.group()) == float(weight):
            pokemons.append(pokemon['name'])
    print(pokemons)


def single_type_candy_count(filename):
    json_file = open(filename, "r", encoding="utf-8")
    pokedex = json.load(json_file)
    json_file.close()
    num_candies = 0
    candies = []
    for pokemon in pokedex['pokemon']:
        try:
            if len(pokemon['type']) == 1 and pokemon['candy_count']:
                candies.append(pokemon['candy'])
                num_candies += int(pokemon['candy_count'])
        except KeyError:
            pass


def reflections_and_projections(points):
    pass



reflections_and_projections([[0, 0], [0, 1]])


"""def normalize(image):
    pass

def sigmoid_normalize(image):
    pass"""
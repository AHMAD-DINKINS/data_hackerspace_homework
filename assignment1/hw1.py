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
        p_weight = re.search(r'[0-9]+\.[0-9]+', pokemon["weight"])
        if float(p_weight.group()) == float(weight):
            pokemons.append(pokemon['name'])


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
    transformed_points = np.array(points)
    projection = 1/10 * np.array([1, 3], [3, 9])
    for row in transformed_points:
        row[1] = -row[1] + 2
    print(transformed_points)
    for row in range(len(transformed_points)):
        transformed_points[row] = [-transformed_points[row][1], transformed_points[row][0]]
    print(transformed_points)



reflections_and_projections([[0, 0], [0, 1]])


"""def normalize(image):
    pass

def sigmoid_normalize(image):
    pass"""
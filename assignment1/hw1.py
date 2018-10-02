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
    return output


def weigh_pokemons(filename, weight):
    json_file = open(filename, "r", encoding="utf-8")
    pokedex = json.load(json_file)
    json_file.close()
    pokemons = []
    for pokemon in pokedex["pokemon"]:
        p_weight = re.search(r'(\d+)\.(\d+)', pokemon["weight"])
        if float(p_weight.group()) == float(weight):
            pokemons.append(pokemon['name'])
    return pokemons


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
    return candies


def reflections_and_projections(points):
    transformed_points = np.copy(points)
    pi_over_2 = np.array([[0, -1], [1, 0]])
    scalar = 1/10
    projection_array = np.array([[1, 3], [3, 9]])
    transformed_points[1] = transformed_points[1] * (-1) + 2
    transformed_points = pi_over_2 @ transformed_points
    transformed_points = scalar * projection_array @ transformed_points
    return transformed_points


def normalize(image):
    maxP = np.amax(image)
    minP = np.amin(image)
    new_image = 255/(maxP - minP)*image-minP
    return new_image


def sigmoid_normalize(image, a):
    new_image = 255 * (1 + np.e**(-a**-1 * (image - 128)))**-1
    return new_image

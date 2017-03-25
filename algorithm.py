from genome import Genome
from parameters import *
from operators import *

def algorithm():
    population = [Genome() for i in range(population_size)]

    for i in range(generation_limit):
        durations = [x.duration for x in population]
        print(" | Generation {:>3}  || best {:>4} | worst {:>4} | avg {:>6.1f} |"
            .format(i+1, min(durations), max(durations), sum(durations) / population_size))

        new_population = []

        if elitism_on:
            new_population.extend(sorted(population, key=lambda x: x.duration)[:2])

        while len(new_population) < population_size:
            (offspring_one, offspring_two) = crossover(*selection(population))
            new_population.append(mutation(offspring_one))
            new_population.append(mutation(offspring_two))

        del population

        population = new_population

from parameters import *
from genome import Genome
from operators import selection, crossover, mutation

# Initialize the first population, out of random genomes.
population = []
for i in range(population_size):
    population.append(Genome())

# Go through 60 generations.
for i in range(generation_limit):
    durations = [x.duration for x in population]
    max_duration = max(durations)
    min_duration = min(durations)
    avg_duration = sum(durations) / len(durations)

    print("Generation {:>3}  ::  best {:>4} | worst {:>4} | avg {:>6.1f}"
        .format(i+1, min_duration, max_duration, avg_duration))
    #print(durations)

    new_population = []

    if elitism_on:
        # The fittest one make it to the new population.
        new_population.extend(sorted(population, key=lambda x: x.duration)[:1])

    while len(new_population) < population_size:
        # Select parents, and crossover them to get 2 offsprings.
        pair_of_offsprings = crossover(*selection(population))

        # Try each offspring for mutation, then append result.
        new_population.append(mutation(pair_of_offsprings[0]))
        new_population.append(mutation(pair_of_offsprings[1]))

    del population

    population = new_population

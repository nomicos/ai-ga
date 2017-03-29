from parameters import *
from random import randint
from genome import Genome

def selection(population):
    # durations = [x.duration for x in population]
    # max_duration = max(durations)
    # fitnesses = sorted([max_duration - x for x in durations])
    population.sort(key=lambda x: x.duration, reverse=True)
    max_duration = population[0].duration

    cdf_vals = [0]
    for i in population[1:]:
        cdf_vals.append((max_duration - i.duration) + cdf_vals[-1])

    i1 = 0
    i2 = 0

    cdf_point = randint(0, cdf_vals[-1])
    for idx, j in enumerate(cdf_vals):
        if cdf_point < j:
            i1 = idx

    cdf_point = randint(0, cdf_vals[-1])
    for idx, j in enumerate(cdf_vals):
        if cdf_point < j:
            i2 = idx

    return (population[i1], population[i2])

def crossover(parent_one, parent_two):
    if randint(0,100) > crossover_rate * 100:
        return (parent_one, parent_two)

    midpoint = randint(1, task_count - 1)

    offspring_one, offspring_two = Genome(False), Genome(False)
    offspring_one.genes = parent_one.genes[:midpoint] + parent_two.genes[midpoint:]
    offspring_two.genes = parent_two.genes[:midpoint] + parent_one.genes[midpoint:]
    offspring_one.update_duration()
    offspring_two.update_duration()

    return (offspring_one, offspring_two)

def mutation(genome):
    for i in range(task_count):
        if randint(0, 100) <= mutation_rate * 100:
            genome.genes[i] = randint(0, resource_count - 1)

    genome.update_duration()
    return genome

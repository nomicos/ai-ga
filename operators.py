from parameters import *
from random import randint
from genome import Genome

def selection(population):
    durations = [x.get_duration() for x in population]
    max_duration = max(durations)

    #print(fitnesses)

    # Accept-reject selection for the first parent.
    safety_counter = 0
    while True:
        safety_counter += 1
        parentA_idx = randint(0, len(population) - 1)
        if randint(0, int(max_duration)) > durations[parentA_idx]:
            break
        if safety_counter > 100:
            break

    # Accept-reject selection for the second parent.
    safety_counter = 0
    while True:
        safety_counter += 1
        parentB_idx = randint(0, len(population) - 1)
        if randint(0, int(max_duration)) > durations[parentB_idx]:
            break
        if safety_counter > 100:
            break

    return (population[parentA_idx], population[parentB_idx])

def crossover(genomeA, genomeB):
    # Note: Lengths of genomes are const and equal.
    midpoint = randint(1, len(genomeA.genes) - 2)
    offspring1 = Genome(False)
    offspring2 = Genome(False)
    offspring1.genes = genomeA.genes[:midpoint] + genomeB.genes[midpoint:]
    offspring2.genes = genomeB.genes[:midpoint] + genomeA.genes[midpoint:]
    return (offspring1, offspring2)

def mutation(genome):
    result = Genome()
    result.genes = genome.genes[:]

    for i in range(len(genome.genes)):
        if randint(0, 100) <= mutation_rate * 100.0:
            result.genes[i] = randint(0, resource_count - 1)

    return result

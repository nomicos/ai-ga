from genome import Genome
from parameters import *
from operators import *




def algorithm() -> tuple:
    population = [Genome() for i in range(population_size)]

    best_stats, worst_stats, avg_stats = [], [], []

    best_genome = population[0]

    for i in range(generation_limit):
        durations = [x.duration for x in population]
        best, worst, avg = min(durations), max(durations), sum(durations) / population_size
        print(" | Generation {:>3}  || best {:>4} | worst {:>4} | avg {:>6.1f} |"
            .format(i+1, best, worst, avg))
        best_stats.append(best)
        worst_stats.append(worst)
        avg_stats.append(avg)

        new_population = []

        if elitism_on:
            new_population.extend(sorted(population, key=lambda x: x.duration)[:2])

        while len(new_population) < population_size:
            (offspring_one, offspring_two) = crossover(*selection(population))
            new_population.append(mutation(offspring_one))
            new_population.append(mutation(offspring_two))

            if offspring_one.duration < best_genome.duration:
                best_genome = offspring_one
            if offspring_two.duration < best_genome.duration:
                best_genome = offspring_two

        del population

        population = new_population

    return best_genome, (best_stats, worst_stats, avg_stats)

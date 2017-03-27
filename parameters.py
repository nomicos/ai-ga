# Duration required by tasks to be completed.
task_durations = [ 24, 40, 22, 23, 22, 24, 18, 17, 10, 23 ]

# The number of tasks; also the length of a genome.
task_count = len(task_durations)

# The number of resources; also the upper bound of a gene value.
resource_count = 7

# How many individuals (genomes) there are in the population.
# Should be even, as the number of offsprings is even.
population_size = 100

# Condition for the algorithm to stop: no. of generation.
generation_limit = 200

# How likely a genome is to mutate.
mutation_rate = 0.03

# How likely a crossover is to occur.
crossover_rate = 0.8

# Flag for elitism.
elitism_on = False

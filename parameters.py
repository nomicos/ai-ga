# Duration required by tasks to be completed.
task_durations = [ 5, 3, 14, 30, 11, 7, 22, 25, 12, 18, 77, 88, 102, 4 ]

# The number of tasks; also the length of a genome.
task_count = len(task_durations)

# The number of resources; also the upper bound of a gene value.
resource_count = 4

# How many individuals (genomes) there are in the population.
# Should be even, as the number of offsprings is even.
population_size = 200

# How likely a genome is to mutate.
mutation_rate = 0.02

# Flag for elitism.
elitism_on = True

from parameters import *
from random import randint

class Genome:
    def __init__(self, random_genes=True):
        self.genes = []
        self.duration = 0

        if random_genes:
            self.generate_random()
            self.update_duration()

    def generate_random(self):
        for i in range(task_count):
            self.genes.append(randint(0, resource_count - 1))

    def update_duration(self):
        workloads = [0] * resource_count

        # For each task, add its duration to the corresponding resource.
        for task_idx, resource_idx in enumerate(self.genes):
            workloads[resource_idx] += task_durations[task_idx]

        # Duration is the time needed for the most loaded resource
        # to complete their job, i.e. the soonest time everyone is done.
        self.duration = max(workloads)

    def __repr__(self):
        return "{} (duration {})\n".format(self.genes, self.duration)

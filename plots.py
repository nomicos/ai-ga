import matplotlib.pyplot as plt
from parameters import generation_limit

x = range(1, generation_limit + 1)

def plot_general(best_stats, worst_stats, avg_stats):
    plt.title("Genetic Algorithm Scheduling Summary")
    plt.plot(x, best_stats, label="Best genome (min duration)", color='green')
    plt.plot(x, worst_stats, label="Worst genome (max duration)", color='red')
    plt.plot(x, avg_stats, label="Average duration of genomes", color='blue')
    plt.xlabel("Generation number")
    plt.ylabel("Duration")
    plt.legend()
    plt.show()

def plot_details(best_stats, worst_stats, avg_stats):
    fig = plt.figure(figsize=(10, 6))

    ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=2)
    ax2 = plt.subplot2grid((3, 3), (2, 0))
    ax3 = plt.subplot2grid((3, 3), (2, 1))
    ax4 = plt.subplot2grid((3, 3), (2, 2))

    plt.tight_layout()

    ax1.set_title("Genetic Algorithm Scheduling Summary")
    ax1.plot(x, worst_stats, label="Worst genome (max duration)", color='red')
    ax1.plot(x, avg_stats, label="Average duration of genomes", color='blue')
    ax1.plot(x, best_stats, label="Best genome (min duration)", color='green')

    ax1.set_ylabel("Duration")
    ax1.legend()

    ax2.plot(x, worst_stats, color='red')
    ax2.set_title("Worst")

    ax3.plot(x, avg_stats, color='blue')
    ax3.set_title("Average")

    ax4.plot(x, best_stats, color='green')
    ax4.set_title("Best")

    plt.show()

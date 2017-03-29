from algorithm import algorithm

from plots import plot_general, plot_details

border_top = '  ' + '_' * 56 + ' \n | ' + '-' * 54 + ' |'
border_bottom = ' | ' + '-' * 54 + ' |\n |' + '_' * 56 + '|'

print(border_top)
winner, stats = algorithm()
print(border_bottom)

print("\n...And the winner is:", winner, sep='\n')

# plot_general(*stats)
plot_details(*stats)

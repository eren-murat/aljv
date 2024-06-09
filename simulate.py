import random
import math
import constants
import creature
import genetic_algo as ga

def create_cells(size):
    coordinates = []
    for x in range(size):
        for y in range(size):
            coordinates.append((x, y))

    return dict.fromkeys(coordinates)

def place_creatures_on_map(population, cells):
    for p in population:
        pos = (random.randint(0, constants.MAP_SIZE - 1), random.randint(0, constants.MAP_SIZE - 1))
        p.update_position(pos)

        if cells[pos] is None:
            cells[pos] = [p]
        else:
            cells[pos].append(p)

    return cells

cells = create_cells(constants.MAP_SIZE)

print("INIT POPULATION")
population = ga.generate_population(constants.INIT_POPULATION_SIZE)
cells = place_creatures_on_map(population, cells)
for p in population:
    p.print_info()

for i in range(constants.NUM_GENERATIONS_SIMULATED):
    print("\n\nGENERATION ", i)
    print("\nSELECT PARENTS")
    parents = ga.select_parents(population, ga.eval_population(population))
    for p in parents:
        p.print_info()

    print("\nCROSSOVER")
    children = ga.crossover(parents, constants.NUM_TRAITS)
    cells = place_creatures_on_map(children, cells)
    for c in children:
        c.print_info()

    print("\nMUTATE")
    mutated_children = [ga.mutate(c, constants.MUTATION_RATE) for c in children]
    for c in mutated_children:
        c.print_info()

    print("\nREBUILD POPULATION")
    # replace the weakest two creatures with the new children
    population = population[0:constants.INIT_POPULATION_SIZE - 2] + mutated_children
    for p in population:
        p.print_info()
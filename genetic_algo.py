import random
import creature
import constants
import utils

def generate_population(size):
     return [creature.Creature() for i in range(size)]

def eval_population(population):
    return [p.eval_creature() for p in population]

def select_parents(population, scores):
    population.sort(key=lambda x: x.score, reverse=True)
    return population[0:2]

def crossover(parents, num_traits):
    point = random.randint(1, num_traits - 1)
    c1_traits = parents[0].traits[:point] + parents[1].traits[point:]
    c2_traits = parents[1].traits[:point] + parents[0].traits[point:]
    c1 = creature.Creature()
    c1.update_traits(c1_traits)
    c2 = creature.Creature()
    c2.update_traits(c2_traits)
    return [c1, c2]

def mutate(child, mutation_rate):
    for i in range(len(child.traits)):
        if random.uniform(0, 1) < mutation_rate:
            child.traits[i] = random.uniform(0, 1)
    child.eval_creature()
    return child

def simple_simulate(population, cells, width, height):
    print("\nSELECT PARENTS")
    parents = select_parents(population, eval_population(population))
    for p in parents:
        p.print_info()

    print("\nCROSSOVER")
    children = crossover(parents, constants.NUM_TRAITS)
    cells = utils.place_creatures_on_map(children, cells, width, height)
    for c in children:
        c.print_info()

    print("\nMUTATE")
    mutated_children = [mutate(c, constants.MUTATION_RATE) for c in children]
    for c in mutated_children:
        c.print_info()

    print("\nREBUILD POPULATION")
    # replace the weakest two creatures with the new children
    population = population[0:constants.INIT_POPULATION_SIZE - 2] + mutated_children
    for p in population:
        p.print_info()

    return population, cells

def dynamic_simulate(population, cells, width, height):
    for p in population:
        pos = p.position
        neighbours = []
        for x in range(-1, 2):
            if x == 0:
                continue
            for y in range(-1, 2):
                if y == 0:
                    continue
                new_x = pos[0] + x
                new_y = pos[1] + y
                if new_x >= 0 and new_x < width and new_y >= 0 and new_y < height:
                    if cells[(new_x, new_y)] is not None:
                        neighbours += cells[(new_x, new_y)]
        p.neighbours = neighbours

        # search for a neighbour with a similar score
        similar_neighbour = get_similar_neighbour(p)

        # crossover with the similar neighbour
        if similar_neighbour is not None:
            print("\nSIMILAR CREATURES MEETING")
            similar_neighbour.print_info()
            p.print_info()

            print("CROSSOVER")
            children = crossover([p, similar_neighbour], constants.NUM_TRAITS)
            for c in children:
                c.print_info()
            cells = utils.place_creatures_on_map(children, cells, width, height)

            print("MUTATE")
            mutated_children = [mutate(c, constants.MUTATION_RATE) for c in children]
            for c in mutated_children:
                c.print_info()

            print("REBUILD POPULATION")
            population.sort(key=lambda x: x.score, reverse=True)
            population = population[0:constants.INIT_POPULATION_SIZE - 2] + mutated_children
            for p in population:
                p.print_info()

    return population, cells

def get_similar_neighbour(creature):
    for n in creature.neighbours:
        if abs(creature.score - n.score) < 0.1:
            return n
    return None
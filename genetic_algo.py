import random
import creature

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
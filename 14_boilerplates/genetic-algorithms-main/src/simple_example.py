""" Simple example of a genetic algorithm """

import random


def individual(length, m, mx):
    return [random.randint(m, mx) for _ in range(length)]


def population(count, length, m, mx):
    return [individual(length, m, mx) for _ in range(count)]


def fitness(individual, target):
    return abs(target - sum(individual))


def population_fitness(pop, target):
    total = sum([fitness(i, target) for i in pop])
    return total / len(pop)


def evolve(pop, target, retain=0.2, random_select=0.05, mutate=0.01):
    graded = [(fitness(x, target), x) for x in pop]
    graded = [x[1] for x in sorted(graded)]
    retain_length = int(len(graded) * retain)
    parents = graded[:retain_length]

    # randomly add other individuals to promote genetic diversity
    for individual in graded[retain_length:]:
        if random_select > random.random():
            parents.append(individual)

    # mutate some individuals
    for individual in parents:
        if mutate > random.random():
            pos_to_mutate = random.randint(0, len(individual) - 1)
            # this mutation is not ideal, because it
            # restricts the range of possible values,
            # but the function is unaware of the min/max
            # values used to create the individuals,
            individual[pos_to_mutate] = random.randint(min(individual), max(individual))

    # crossover parents to create children
    parents_length = len(parents)
    desired_length = len(pop) - parents_length
    children = []
    while len(children) < desired_length:
        male = random.randint(0, parents_length - 1)
        female = random.randint(0, parents_length - 1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = int(len(male) / 2)
            child = male[:half] + female[half:]
            children.append(child)

    parents.extend(children)
    return parents


def test_genetic_example():
    target = 371
    p_count = 100
    i_length = 5
    i_min = 0
    i_max = 100

    p = population(p_count, i_length, i_min, i_max)
    fitness_history = [population_fitness(p, target)]

    for i in range(100):
        p = evolve(p, target)
        fitness_history.append(population_fitness(p, target))
        if population_fitness(p, target) == 0:
            print('Done')
            print(len(p))
            break

    print(fitness_history)


if __name__ == '__main__':
    test_genetic_example()

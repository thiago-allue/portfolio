import time
import random
import operator

import matplotlib.pyplot as plt


def fitness(password, test_word):
    score = 0
    i = 0
    while i < len(password):
        if password[i] == test_word[i]:
            score += 1
        i += 1
    return score * 100 / len(password)


def generate_word(length):
    i = 0
    result = ""
    while i < length:
        letter = chr(97 + int(26 * random.random()))
        result += letter
        i += 1
    return result


def generate_population(size, password):
    population = []
    i = 0
    while i < size:
        population.append(generate_word(len(password)))
        i += 1
    return population


def calculate_fitness(population, password):
    population_perf = {}
    for individual in population:
        population_perf[individual] = fitness(password, individual)
    return sorted(population_perf.items(), key=operator.itemgetter(1), reverse=True)


def selection_from_population(sorted_population, best_sample, lucky_few):
    next_generation = []

    for i in range(best_sample):
        next_generation.append(sorted_population[i][0])

    for i in range(lucky_few):
        next_generation.append(random.choice(sorted_population)[0])

    random.shuffle(next_generation)
    return next_generation


def create_child(individual1, individual2):
    child = ""
    for i in range(len(individual1)):
        if random.random() < 0.5:
            child += individual1[i]
        else:
            child += individual2[i]
    return child


def create_children(breeders, number_of_child):
    next_population = []
    for i in range(int(len(breeders) / 2)):
        for j in range(number_of_child):
            next_population.append(
                create_child(breeders[i], breeders[len(breeders) - 1 - i])
            )
    return next_population


def mutate_word(word):
    index_modification = int(random.random() * len(word))
    if index_modification == 0:
        word = chr(97 + int(26 * random.random())) + word[1:]
    else:
        word = (
            word[:index_modification]
            + chr(97 + int(26 * random.random()))
            + word[index_modification + 1 :]
        )
    return word


def mutate_population(population, chance_of_mutation):
    for i in range(len(population)):
        if random.random() * 100 < chance_of_mutation:
            population[i] = mutate_word(population[i])
    return population


def next_generation(
    first_generation,
    password,
    best_sample,
    lucky_few,
    number_of_child,
    chance_of_mutation,
):
    sorted_population = calculate_fitness(first_generation, password)
    next_breeders = selection_from_population(sorted_population, best_sample, lucky_few)
    next_population = create_children(next_breeders, number_of_child)
    next_generation_pop = mutate_population(next_population, chance_of_mutation)
    return next_generation_pop


def multiple_generation(
    number_of_generation,
    password,
    size_population,
    best_sample,
    lucky_few,
    number_of_child,
    chance_of_mutation,
):
    historic = []
    historic.append(generate_population(size_population, password))
    for i in range(number_of_generation):
        historic.append(
            next_generation(
                historic[i],
                password,
                best_sample,
                lucky_few,
                number_of_child,
                chance_of_mutation,
            )
        )
    return historic


def report(historic, password, number_of_generation):
    result = get_best_individuals_historic(historic, password)[
        number_of_generation - 1
    ]
    print("solution: \"" + result[0] + "\" de fitness: " + str(result[1]))


def get_best_individual_from_population(population, password):
    return calculate_fitness(population, password)[0]


def get_best_individuals_historic(historic, password):
    best_individuals = []
    for population in historic:
        best_individuals.append(
            get_best_individual_from_population(population, password)
        )
    return best_individuals


def evolution_best_fitness(historic, password):
    plt.axis([0, len(historic), 0, 105])
    plt.title(password)

    evolution_fitness = []
    for population in historic:
        evolution_fitness.append(
            get_best_individual_from_population(population, password)[1]
        )
    plt.plot(evolution_fitness)
    plt.ylabel('fitness best individual')
    plt.xlabel('generation')
    plt.show()


def evolution_avg_fitness(historic, password, size_population):
    plt.axis([0, len(historic), 0, 105])
    plt.title(password)

    evolution_fitness = []
    for population in historic:
        population_perf = calculate_fitness(population, password)
        avg_fitness = 0
        for individual in population_perf:
            avg_fitness += individual[1]
        evolution_fitness.append(avg_fitness / size_population)
    plt.plot(evolution_fitness)
    plt.ylabel('Average fitness')
    plt.xlabel('generation')
    plt.show()


def test_password():
    password = "onlylettersnospacesforpasswordthiscanbechanged"
    size_population = 1000
    best_sample = 200
    lucky_few = 200
    number_of_child = 5
    number_of_generation = 100
    chance_of_mutation = 5

    temps1 = time.time()

    if ((best_sample + lucky_few) / 2 * number_of_child) != size_population:
        print("Population size not stable")
    else:
        historic = multiple_generation(
            number_of_generation,
            password,
            size_population,
            best_sample,
            lucky_few,
            number_of_child,
            chance_of_mutation,
        )

        report(historic, password, number_of_generation)

        evolution_best_fitness(historic, password)
        evolution_avg_fitness(historic, password, size_population)

    print(time.time() - temps1)


if __name__ == '__main__':
    test_password()

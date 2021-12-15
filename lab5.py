import copy
import math
import random
import matplotlib.pyplot as plt

# Каждый массив - продукт с характеристиками: белки, жиры, углеводы, калории
products = [
    [5.0, 7.8, 4.2, 289],
    [3.8, 8.7, 1.5, 123],
    [4.1, 7.3, 2.9, 666],
    [2.1, 9.1, 8.6, 291],
    [3.5, 8.1, 7.1, 560],
    [9.7, 0.6, 9.7, 347],
    [9.4, 2.1, 6.4, 343],
    [1.4, 4.1, 4.4, 507],
    [6.5, 9.5, 3.1, 337],
    [6.9, 3.6, 8.2, 556]
]

prices = [698, 876, 941, 230, 249, 269, 612, 287, 884, 482]

chromosomes = [
    [0, 0, 0, 0, 1, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 1, 1, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1]
]

chromosomes_count = 5

standard = [50, 20, 50, 1500]


def calculate_price(_chromosome):
    price = 0
    for i in range(len(_chromosome)):
        if _chromosome[i] == 1:
            price += prices[i]
    return price


def fitness(_chromosome):
    temp_characteristics = [0, 0, 0, 0]
    for i in range(len(_chromosome)):
        if _chromosome[i] == 1:
            for characteristic_index in range(len(temp_characteristics)):
                temp_characteristics[characteristic_index] += products[i][characteristic_index]

    percent_differences = [0, 0, 0, 0]

    for characteristic_index in range(len(temp_characteristics)):
        percent_differences[characteristic_index] = abs(temp_characteristics[characteristic_index] -
                                                        standard[characteristic_index]) / standard[characteristic_index]

    percent_fitness = 0

    for percent_difference_index in range(len(percent_differences)):
        percent_fitness += percent_differences[percent_difference_index]

    return percent_fitness


def select_chromosomes(_chromosomes):
    sorted_chromosomes = sorted(_chromosomes.items(), key=lambda x: x[0])

    surviving_chromosomes = {}

    for i in range(math.ceil(len(sorted_chromosomes) * 0.7)):
        surviving_chromosomes[fitness(sorted_chromosomes[i][1])] = \
            sorted_chromosomes[i][1]

    return surviving_chromosomes


def cross_chromosomes(_chromosomes):
    crossed_chromosomes = {}

    v1 = []
    v2 = []

    index = 0

    for _chromosome in _chromosomes.items():

        # поменять скрещивание

        if index == 0:
            v1 = _chromosome[1]
            index += 1
            continue

        if index == 1:
            v2 = _chromosome[1]
            index += 1

        if index == 2:
            child_chromosome_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            child_chromosome_1[0] = v1[0]
            child_chromosome_1[1] = v1[1]
            child_chromosome_1[2] = v2[2]
            child_chromosome_1[3] = v2[3]
            child_chromosome_1[4] = v1[4]
            child_chromosome_1[5] = v1[5]
            child_chromosome_1[6] = v2[6]
            child_chromosome_1[7] = v2[7]
            child_chromosome_1[8] = v1[8]
            child_chromosome_1[9] = v1[9]

            child_chromosome_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            child_chromosome_2[0] = v2[0]
            child_chromosome_2[1] = v2[1]
            child_chromosome_2[2] = v1[2]
            child_chromosome_2[3] = v1[3]
            child_chromosome_2[4] = v2[4]
            child_chromosome_2[5] = v2[5]
            child_chromosome_2[6] = v1[6]
            child_chromosome_2[7] = v1[7]
            child_chromosome_2[8] = v2[8]
            child_chromosome_2[9] = v2[9]

            check_and_set(child_chromosome_1, _chromosomes, crossed_chromosomes)
            check_and_set(child_chromosome_2, _chromosomes, crossed_chromosomes)

            index = 0

    i = 1
    j = 1

    temp_chromesome = copy.copy(crossed_chromosomes)

    for _chromosome in temp_chromesome.items():
        if crossed_chromosomes.__len__() > chromosomes_count:
            crossed_chromosomes.__delitem__(_chromosome[0])

    for _chromosome in crossed_chromosomes.items():
        _chromosomes[_chromosome[0]] = _chromosome[1]
         

    return _chromosomes


def check_and_set(child_chromosome, _chromosomes, crossed_chromosomes):
    key = fitness(child_chromosome)
    if key not in _chromosomes:
        crossed_chromosomes[key] = child_chromosome


def mutate_chromosomes(_chromosomes):
    for i in range(3):

        random_chromosome = random.randint(0, len(_chromosomes) - 1)
        random_gen = random.randint(0, len(products) - 1)

        index = 0
        for _chromosome in _chromosomes.items():
            if index == random_chromosome:
                if _chromosome[1][random_gen] == 0:
                    _chromosome[1][random_gen] = 1
                else:
                    _chromosome[1][random_gen] = 0
                break
            index += 1
    return _chromosomes


def print_chromosomes(_chromosomes, i):
    for key, value in _chromosomes.items():
        print("Итерация: ", i, ". Отклонение: ", round(key, 1), ". Набор хромосом: ", value)
        print("Количество хромосом: ", len(_chromosomes))


def start():
    cycle_chromosomes = {}

    best_chromosome = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    best_fitness = 100
    max_price = 10000
    step = 0
    iteration = 1
    common_fitness_array = []
    best_fitness_array = []

    for i in range(len(chromosomes)):
        cycle_chromosomes[fitness(chromosomes[i])] = chromosomes[i]

    print("Изначальный набор хромосом:")
    for key, value in cycle_chromosomes.items():
        print(" Отклонение: ", round(key, 1), ". Набор хромосом: ", value)

    while step < 50:
        cycle_chromosomes = select_chromosomes(cycle_chromosomes)
        cycle_chromosomes = cross_chromosomes(cycle_chromosomes)
        cycle_chromosomes = mutate_chromosomes(cycle_chromosomes)

        print_chromosomes(cycle_chromosomes, iteration)
        print("Количество хромосом: ", len(cycle_chromosomes))

        sum_fitness = 0

        for _chromosome in cycle_chromosomes.items():
            sum_fitness += _chromosome[0]

        common_fitness = sum_fitness / len(cycle_chromosomes)

        common_fitness_array.append(common_fitness)

        new_best_chromosome = False

        for _chromosome in cycle_chromosomes.items():

            if calculate_price(_chromosome[1]) < max_price:
                if fitness(_chromosome[1]) < best_fitness:
                    for i in range(5):
                        best_chromosome[i] = _chromosome[1][i]
                    best_fitness = fitness(_chromosome[1])
                    step = 0
                    new_best_chromosome = True
                    print("Новая лучшая хромосома: ", best_chromosome, ". Отклонение от эталона: ", best_fitness)

        if not new_best_chromosome:
            step += 1

        iteration += 1

        best_fitness_array.append(best_fitness)

    print("Лучшая хромосома: ", best_chromosome)
    print("Ее отклонение от эталона: ", best_fitness)

    plt.plot(common_fitness_array, color='blue')
    plt.plot(best_fitness_array, color='green')
    plt.xlabel('Поколение')
    plt.ylabel('Отклонение от эталона')
    plt.legend(['Среднее отклонение от эталона', 'Минимальное отклонение от эталона'])
    plt.title('Зависимость "Отклонения от эталона" от "Поколения"')
    plt.show()

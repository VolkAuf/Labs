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

# Цены на продукты
prices = [698, 876, 941, 230, 249, 269, 612, 287, 884, 482]

# Набор хромосом (каждый массив - рацион из 10 продуктов)
chromosomes = [
    [0, 0, 0, 0, 1, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 1, 1, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1]
]

# Эталон по суммарному количеству Белков, Жиров, Углеводов и Ккал
standard = [50, 20, 50, 1500]


# Высчитать цену покупки
def calculate_price(_chromosome):
    # print(_chromosome)
    price = 0
    for i in range(len(_chromosome)):
        if _chromosome[i] == 1:
            price += prices[i]
    # print("Цена покупки: ", price)
    return price


# Высчитать коэффициент приспособленности
def fitness(_chromosome):
    temp_characteristics = [0, 0, 0, 0]
    for i in range(len(_chromosome)):
        if _chromosome[i] == 1:
            for characteristic_index in range(len(temp_characteristics)):
                temp_characteristics[characteristic_index] += products[i][characteristic_index]
    # print(f'\nХарактеристики получившейся хромосомы: {temp_characteristics}')

    percent_differences = [0, 0, 0, 0]

    for characteristic_index in range(len(temp_characteristics)):
        percent_differences[characteristic_index] = abs(temp_characteristics[characteristic_index] -
                                                        standard[characteristic_index]) / standard[characteristic_index]

    # print(f'\nПроцентные отклонения: {percent_differences}')

    percent_fitness = 0

    for percent_difference_index in range(len(percent_differences)):
        percent_fitness += percent_differences[percent_difference_index]

    # print(f'\nОтклонение хромосомы от эталона: {percent_fitness}')

    return percent_fitness


# Выбрать лучшие хромосомы
def select_chromosomes(_chromosomes):
    sorted_chromosomes = sorted(_chromosomes.items(), key=lambda x: x[0])

    surviving_chromosomes = {}

    # передавать саму хромасому
    for _chromosome_index in range(math.ceil(len(sorted_chromosomes) * 0.7)):
        surviving_chromosomes[fitness(sorted_chromosomes[_chromosome_index][1])] = \
            sorted_chromosomes[_chromosome_index][1]

    return surviving_chromosomes


# Скрестить хромосомы
def cross_chromosomes(_chromosomes):

    crossed_chromosomes = {}

    chr_1_val = []
    chr_2_val = []

    index = 0

    for _chromosome in _chromosomes.items():

        # поменять скрещивание

        if index == 0:
            chr_1_val = _chromosome[1]
            index += 1
            continue

        if index == 1:
            chr_2_val = _chromosome[1]
            index += 1
            # continue

        if index == 2:
            child_chromosome_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            child_chromosome_1[0] = chr_1_val[0]
            child_chromosome_1[1] = chr_1_val[1]
            child_chromosome_1[2] = chr_2_val[2]
            child_chromosome_1[3] = chr_2_val[3]
            child_chromosome_1[4] = chr_1_val[4]
            child_chromosome_1[5] = chr_1_val[5]
            child_chromosome_1[6] = chr_2_val[6]
            child_chromosome_1[7] = chr_2_val[7]
            child_chromosome_1[8] = chr_1_val[8]
            child_chromosome_1[9] = chr_1_val[9]

            child_chromosome_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            child_chromosome_2[0] = chr_2_val[0]
            child_chromosome_2[1] = chr_2_val[1]
            child_chromosome_2[2] = chr_2_val[2]
            child_chromosome_2[3] = chr_2_val[3]
            child_chromosome_2[4] = chr_2_val[4]
            child_chromosome_2[5] = chr_1_val[5]
            child_chromosome_2[6] = chr_1_val[6]
            child_chromosome_2[7] = chr_1_val[7]
            child_chromosome_2[8] = chr_1_val[8]
            child_chromosome_2[9] = chr_1_val[9]

            # вынести в метод

            key_1 = fitness(child_chromosome_1)
            if key_1 not in _chromosomes:
                crossed_chromosomes[key_1] = child_chromosome_1

            key_2 = fitness(child_chromosome_2)
            if key_2 not in _chromosomes:
                crossed_chromosomes[key_2] = child_chromosome_2
            index = 0

    for _chromosome in crossed_chromosomes.items():
        _chromosomes[_chromosome[0]] = _chromosome[1]

    return _chromosomes


# Мутировать одну их хромосом
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


def start_evolution():
    cycle_chromosomes = {}

    for _chromosome_index in range(len(chromosomes)):
        cycle_chromosomes[fitness(chromosomes[_chromosome_index])] = chromosomes[_chromosome_index]

    print("Изначальный набор хромосом:", cycle_chromosomes)

    # Лучшая хромосома
    best_chromosome = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Лучшая приспособленность
    best_fitness = 100

    # Максимальная допустимая цена (Сумма продуктов рациона не должна ее превышать)
    acceptable_price = 10000

    step = 0

    iteration = 1

    common_fitness_array = []
    best_fitness_array = []

    while step < 10:
        cycle_chromosomes = select_chromosomes(cycle_chromosomes)
        cycle_chromosomes = cross_chromosomes(cycle_chromosomes)
        cycle_chromosomes = mutate_chromosomes(cycle_chromosomes)
        print("Итерация: ", iteration, ". Набор хромосом: ", cycle_chromosomes)
        print("Количество хромосом: ", len(cycle_chromosomes))

        sum_fitness = 0

        for _chromosome in cycle_chromosomes.items():
            sum_fitness += _chromosome[0]

        common_fitness = sum_fitness / len(cycle_chromosomes)

        common_fitness_array.append(common_fitness)

        new_best_chromosome = False

        for _chromosome in cycle_chromosomes.items():

            if calculate_price(_chromosome[1]) < acceptable_price:
                if fitness(_chromosome[1]) < best_fitness:
                    for i in range(10):
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

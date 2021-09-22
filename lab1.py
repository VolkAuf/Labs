import numpy as np
import pandas as pd
import random
import cowsay as sas

table_size = 1000


def generate_noise(noise, arr):
    for i in range(random.randint(0, table_size)):
        be_or_not_be = random.randint(0, 10)
        if be_or_not_be > 7:
            line = random.randint(0, table_size - 1)
            if arr[line] != np.nan:
                head = int(arr[line])
                tail = int(arr[line] + noise)
                arr[line] = random.randint(head, tail)


def float_to_int(arr):
    for i in range(1000):
        arr[i] = round(arr[i], 0)
        arr[i] = int(arr[i])


def generate_nan(arr):
    for i in range(random.randint(0, table_size)):
        be_or_not_be = random.randint(0, 10)
        if be_or_not_be > 8:
            line = random.randint(0, table_size - 1)
            arr[line] = np.nan


def start_lab1():
    akkum = np.random.normal(4000, 2000, table_size)
    float_to_int(akkum)
    generate_noise(10000, akkum)
    generate_nan(akkum)

    cam_pix = np.random.normal(8, 4, table_size)
    float_to_int(cam_pix)
    generate_noise(130, cam_pix)
    generate_nan(cam_pix)

    ram = np.random.randint(2000, 6000, table_size) * 0.1
    float_to_int(ram)
    generate_noise(64, ram)
    generate_nan(ram)

    rom = np.random.exponential(4000, table_size)
    float_to_int(rom)
    generate_noise(1024, rom)
    generate_nan(rom)

    my_table = {'Аккумулятор ': akkum, 'Пиксели камеры ': cam_pix, 'ПЗУ ': rom, 'ОЗУ ': ram}

    df = pd.DataFrame(data=my_table)
    df.to_csv("data.csv", index=False)

    sas.cow("Задания:")

    sas.cow("1  - Среднее значение по аккумуляторам")
    sas.cow("2 - Максимально мегапикселей:")
    sas.cow("3 - Минимально ПЗУ:")

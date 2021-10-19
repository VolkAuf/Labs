import numpy as np
import pandas as pd
import random
import cowsay as sas

table_size = 500


def generate_noise(noise, arr):
    for i in range(random.randint(0, table_size)):
        be_or_not_be = random.randint(0, 10)
        if be_or_not_be > 9:
            line = random.randint(0, table_size - 1)
            if arr[line] != np.nan:
                head = int(arr[line])
                tail = int(arr[line] + noise)
                arr[line] = random.randint(head, tail)


def float_to_int(arr):
    for i in range(table_size):
        arr[i] = round(arr[i], 0)
        arr[i] = int(arr[i])


def generate_nan(arr):
    for i in range(random.randint(0, table_size)):
        be_or_not_be = random.randint(0, 10)
        if be_or_not_be > 9:
            line = random.randint(0, table_size - 1)
            arr[line] = np.nan


def start_lab1():
    akkum = np.random.normal(4000, 1000, table_size)
    float_to_int(akkum)
    generate_noise(10000, akkum)
    generate_nan(akkum)

    cam_pix = np.random.normal(8, 2, table_size)
    float_to_int(cam_pix)
    generate_noise(130, cam_pix)
    generate_nan(cam_pix)

    rom = np.random.randint(32, 128,  table_size) * 0.1 * 10
    float_to_int(rom)
    generate_noise(524, rom)
    generate_nan(rom)

    ram = np.random.exponential(2, table_size) + 1
    float_to_int(ram)
    generate_noise(64, ram)
    generate_nan(ram)



    # my_table = {'Аккумулятор ': akkum}
    # , 'Пиксели камеры ': cam_pix, 'ПЗУ ': rom, 'ОЗУ ': ram
    # =СЧЁТЕСЛИ(A2:A501;(">6000"))+СЧЁТЕСЛИ(A2:A501;("<2000"))

    my_table = {'Аккумулятор ': akkum, 'Пиксели камеры ': cam_pix, 'ПЗУ ': rom, 'ОЗУ ': ram}

    df = pd.DataFrame(data=my_table)
    df.to_csv("data.csv", index=False)

    sas.cow("Задания:")

    sas.cow("1  - Среднее значение по аккумуляторам")
    sas.cow("2 - Максимально мегапикселей:")
    sas.cow("3 - Минимально ПЗУ:")

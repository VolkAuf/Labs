import numpy as np
import pandas as pd
import random
import cowsay as sas
from pandas import DataFrame

chill_time_s = 'Время отдыха'
salary_s = 'Зарплата'
seniority_s = 'Стаж'
worked_time_s = 'Отработанные часы'


def normalized_function(array):

    temp_array = array
    temp_array = [el for el in temp_array if not np.isnan(el)]
    temp_array.sort()

    lower_quartile = np.quantile(temp_array, 0.25)
    upper_quartile = np.quantile(temp_array, 0.75)

    range_quartile = lower_quartile - upper_quartile

    lower_inner_fence = lower_quartile + 1.5 * range_quartile
    upper_inner_fence = upper_quartile - 1.5 * range_quartile

    median_value = np.median(temp_array)

    return list(map(lambda x: x if lower_inner_fence <= x <= upper_inner_fence else median_value, array))


def start_lab2():
    table = pd.read_csv('dataSoseda.csv')

    chill_time_array = table[chill_time_s].to_list()
    salary_array = table[salary_s].to_list()
    seniority_array = table[seniority_s].to_list()
    worked_time_array = table[worked_time_s].to_list()

    chill_time_array = normalized_function(chill_time_array)
    salary_array = normalized_function(salary_array)
    seniority_array = normalized_function(seniority_array)
    worked_time_array = normalized_function(worked_time_array)

    new_table = pd.DataFrame({chill_time_s: chill_time_array, salary_s: salary_array, seniority_s: seniority_array,
                              worked_time_s: worked_time_array})

    new_table.to_csv("dataSoseda_New.csv", index=False)

    print(new_table[chill_time_s].mean())
    print(new_table[salary_s].min())
    print(new_table[seniority_s].max())

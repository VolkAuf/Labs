import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

chill_time_s = 'Время отдыха'
salary_s = 'Зарплата'
seniority_s = 'Стаж'
worked_time_s = 'Отработанные часы'


def start():

    table = pd.read_csv('dataSoseda_New.csv')

    # получаем данные
    x = np.array(table[chill_time_s]).reshape((-1, 1))
    y = np.array(table[salary_s])

    # строим модель
    model = LinearRegression()
    model.fit(x, y)

    # детерминация
    r_sq = model.score(x, y)

    # Ожидание
    prediction = model.predict(x)

    # регаем график
    sns.regplot(x=x, y=y)

    # строим график регрессионной модели
    sns.regplot(x=x, y=prediction)

    plt.xlabel('Время отдыха')
    plt.ylabel('Зарплата')

    print('Коэффициент детерминации = ', str(r_sq))

    plt.show()
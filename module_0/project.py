#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np

def game_core_v3(number):
    '''Создаем переменные с максимальным и минимальным значениями диапозона чисел.
  Устанавливаем любое random число, а затем записываем его в нижний или верхний 
  предел диапазона в зависимости от того меньше оно или больше нужного соответственно. 
  Получаем новый, уменьшенный диапазон, в котором находится загаданное число. После этого 
  делим новый диапазон пополам (находим его среднее значение). Это будет следующее предполагаемое число. И так далее.'''
    count = 1
    max = 100
    min = 1
    predict = np.random.randint(1, 101)
    while predict != number:
        count+=1
        if predict < number:
           min = predict
           predict = int(round((max + min)/2))
        elif predict > number:
           max = predict
           predict = int((max + min)/2)
    return (count)

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# Проверяем
score_game(game_core_v3)


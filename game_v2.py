"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def shrinking_predict(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь

    count = 0   # счетчик попыток
    prdict_number_min = 1  # нижняя граница поиска числа
    prdict_number_max = 101  # верхняя граница поиска числа
    
    while True:
        count+=1
        
        prdict_number = (prdict_number_max + prdict_number_min) // 2

        if number > prdict_number:
            prdict_number_min = prdict_number  # смещение нижней границы поиска числа

        elif number < prdict_number:
            prdict_number_max = prdict_number  # смещение верхней границы поиска числа

        else:
            break

    # Ваш код заканчивается здесь

    return count


def score_game(shrinking_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(shrinking_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(shrinking_predict)

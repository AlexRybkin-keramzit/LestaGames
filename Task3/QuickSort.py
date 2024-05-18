from typing import List
from random import choice

"""
Вопрос №3

На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. 
Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить, 
почему вы считаете, что функция соответствует заданным критериям.
"""


def sort(container: List[int]) -> List[int]:
    """
    Quick sort algorithm.

    :param container: sequence to be sorted.
    :return: sorted sequence in ascending order.
    """
    if len(container) <= 1:
        return container

    reference = choice(container)

    return (
            sort([elem for elem in container if elem < reference]) +
            [elem for elem in container if elem == reference] +
            sort([elem for elem in container if elem > reference])
    )

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


"""
Данный вариант сортировки имеет сложность:
    O(n∗log(n))  в среднем и лучшем случае,
    O(n2)  в худшем случае.
Приведенный алгоритм не создает дополнительные контейнеры данных, а сортирует последовательность в имеющемся массиве.  
Подобный метод является сортировкой по-умолчанию на языке java, а также на данном методе реализована функция qsort() на 
языке C.
"""

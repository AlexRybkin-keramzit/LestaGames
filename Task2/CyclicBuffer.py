from typing import Any

"""
Вопрос №2

На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой 
реализации.

Оценивается:

1. Полнота и качество реализации
2. Оформление кода
3. Наличие сравнения и пояснения по быстродействию
"""


class CycleBuffer:
    def __init__(self, size: int):
        self.buffer = []
        self.size = size

    def push(self, item: Any) -> None:
        """
        Add item in the end of queue.

        :param item: Element to be added.
        """
        if len(self.buffer) == self.size:
            self.buffer.pop(0)
        self.buffer.append(item)

    def get(self) -> Any:
        """
        Extract an item from the beginning.

        :raise: IndexError - If the queue is empty.

        :return: Item from the beginning.
        """

        if not self.buffer:
            raise IndexError('List is empty')
        return self.buffer.pop(0)

    def peek(self, ind: int = 0) -> Any:
        """
        Show the ind item without dequeue.
        :param ind: Index of the item, like in list.

        :raise: TypeError - if ind is not int.
        :raise: IndexError - if index is out of the queue.

        :return: Ind item.
        """
        if not isinstance(ind, int):
            raise TypeError(f'Index must be int, not {type(ind)}')
        if not 0 <= ind < len(self.buffer):
            raise IndexError('There is no such index')
        return self.buffer[ind]

    def clear(self) -> None:
        """Clearing the buffer."""
        self.buffer.clear()

    def is_empty(self):
        """Checking for elements."""
        if self.buffer:
            return 'There is something here...'
        else:
            return 'Everything has disappeared somewhere...'

    def show_buffer(self):
        """Shows the whole buffer."""
        return self.buffer


if __name__ == '__main__':
    pass

"""
Priority Queue
Queue priorities are from 0 to 10
"""
from typing import Any

from collections import deque


class PriorityQueue:
    HIGH_PRIORITY = 0  # наивысший приоритет
    LOW_PRIORITY = 10  # наименьший приоритет

    def __init__(self):
        self._queue = []
        for _ in range(11):
            self._queue.append([])
        print(self._queue)
          # TODO использовать deque для реализации очереди с приоритетами

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Добавление элемент в конец очереди c учетом приоритета

        :param elem: Элемент, который должен быть добавлен
        :param priority: Приоритет добавляемого элемента
        """
        self._queue[priority].append(elem)  # TODO реализовать метод enqueue

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """

        for i in range(11):
            if not self._queue[i]:
                raise IndexError
            if self._queue[i]:
                return self._queue[i].pop()  # TODO реализовать метод dequeue

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди с указанным приоритетом, и т.д.)
        :param priority: Приоритет очереди

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError("должны быть только цифры в индексе")
        if not self._queue[priority]:
            raise ValueError("нет элементов с этим приоритетом")
        if 0 < ind < len(self._queue[priority]):
            raise ValueError("нет такого индекса в этом приаретере")

        return self._queue[priority][ind] # TODO реализовать метод peek

    def clear(self) -> None:
        """ Очистка очереди. """
        for i in range(11):
            self._queue[i].clear()  # TODO реализовать метод clear

    def __len__(self):
        """ Количество элементов в очереди. """
        len_ = 0
        for i in range(11):
            print(self._queue[i])
            len_ = len_ + len(self._queue[i])

        return len_ # TODO реализовать метод __len__

if __name__ == "__main__":
    a = PriorityQueue()
    a.enqueue("aaa", 0)
    a.enqueue("asfq",0)
    a.enqueue("kkkkk", 3)
    a.enqueue("sssss", 3)
    a.enqueue("tttt", 4)
    print(a._queue)
    # print(a.dequeue())
    print(a.dequeue())
    print(a.dequeue())
    # print(a.dequeue())
    # print(a.__len__())
    # a.clear()
    print(a._queue)
    print(a.peek(0, 3))
    print(len(a))